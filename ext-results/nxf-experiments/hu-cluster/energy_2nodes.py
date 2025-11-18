import sys
import pandas as pd


# Constants
rapl_max_value_overflow = 262143328850
rapl_DRAM_max_value_overflow = 65712999613
energy_unit_joules = 1e-6  # 1 µJ converted to joules -> Most probably the correct scaling factor for Intel(R) Xeon(R) Silver 4314 CPU
PKG = 'pkg'
DRAM = 'dram'
args = sys.argv[1:]
workflow = args[0]
run_data = {} 

with open(f'{workflow}/stamps.csv') as file:
    stamps = [line.rstrip().split(',') for line in file.readlines()][1:]

runs = len(stamps)

for run in range(0, runs):
    run_data[run] = {}
    run_data[run]['start'] = int(stamps[run][1])
    run_data[run]['end'] = int(stamps[run][2])


# Functions
def get_energy_data(pkg_file, dram_file):
    with open(pkg_file) as file:
        stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
        header = stripped_lines[0]
        data = stripped_lines[1:]

    pkg_df = pd.DataFrame(data, columns=header)
    pkg_df['timestamp'] = pkg_df['timestamp'].astype(int)
    pkg_df['energy'] = pkg_df['energy'].astype(float)

    with open(dram_file) as file:
        stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
        dram_data = stripped_lines[1:]

    dram_df = pd.DataFrame(dram_data, columns=header)
    dram_df['timestamp'] = dram_df['timestamp'].astype(int)
    dram_df['energy'] = pkg_df['energy'].astype(float)

    return pkg_df, dram_df


def convert_J_to_kWh(joules):
    return joules / 3600000


def get_idle_period_data(run, node):
    energy_dir = f'{workflow}/{run+1}/energy/'
    with open(energy_dir + f'idle_{node}.csv') as file:
        stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
        header = stripped_lines[0]
        data = stripped_lines[1:]

    idle_periods = pd.DataFrame(data, columns=header).drop(columns=['start_time', 'end_time'])
    idle_periods['start_ms'] = idle_periods['start_ms'].astype(float)
    idle_periods['end_ms'] = idle_periods['end_ms'].astype(float)
    return idle_periods


def get_rapl_for_period(start_time, end_time, package_log, dram_log):
    calculated_consumption = False 
    position = 0
    start_point_found = False
    energy_consumed = 0
    start_energy = 0
    overflows = 0

    while not calculated_consumption and position < len(package_log):
        if not start_point_found:
            if start_time <= package_log[position][0]:
                start_point_found = True
                start_energy = package_log[position][1]
                position = position - 1
        else:
            if package_log[position][1] < package_log[position - 1][1]:
                overflows += 1
            if end_time <= package_log[position][0]: 
                energy_consumed = (package_log[position][1] + (overflows * rapl_max_value_overflow) - start_energy) * energy_unit_joules
                calculated_consumption = True
        position += 1

    if not calculated_consumption:
        energy_consumed = (package_log[-1][1] + (overflows * rapl_max_value_overflow) - start_energy) * energy_unit_joules

    calculated_consumption = False 
    position = 0
    start_point_found = False
    dram_energy_consumed = 0
    start_energy = 0
    overflows = 0

    while not calculated_consumption and position < len(dram_log):
        if not start_point_found:
            if start_time <= dram_log[position][0]:
                start_point_found = True
                start_energy = dram_log[position][1]
                position = position - 1
        else:
            if dram_log[position][1] < dram_log[position - 1][1]:
                overflows += 1
            if end_time <= dram_log[position][0]: 
                dram_energy_consumed = (dram_log[position][1] + (overflows * rapl_DRAM_max_value_overflow) - start_energy) * energy_unit_joules
                calculated_consumption = True
        position += 1

    if not calculated_consumption:
        dram_energy_consumed = (dram_log[-1][1] + (overflows * rapl_DRAM_max_value_overflow) - start_energy) * energy_unit_joules

    return (energy_consumed, dram_energy_consumed)


with open(f'{workflow}-runs.csv', 'w') as outfile:
    outfile.write('run,pkg,dram,total\n')

    for run in range(0, runs): 
        task_data = []
        trace = f'{workflow}/{run+1}/trace.csv'
        energy_dir = f'{workflow}/{run+1}/energy/'
        pkg_c37 = energy_dir + f'run_{run+1}_c37_pkg.csv'
        pkg_c38 = energy_dir + f'run_{run+1}_c38_pkg.csv'
        dram_c37 = energy_dir + f'run_{run+1}_c37_dram.csv'
        dram_c38 = energy_dir + f'run_{run+1}_c38_dram.csv'

        # store trace run data
        with open(trace) as file:
            stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
            header = stripped_lines[0]
            data = stripped_lines[1:]

        workflow_start = run_data[run]['start']
        workflow_end = run_data[run]['end']
        run_df = pd.DataFrame(data, columns=header)
        run_df['start'] = run_df['start'].astype(int)
        run_df['complete'] = run_df['complete'].astype(int)
        c37_pkg, c37_dram = get_energy_data(pkg_c37, dram_c37)
        c38_pkg, c38_dram = get_energy_data(pkg_c38, dram_c38)
        energy_by_host = {
            'hu-worker-c37': {
                PKG: c37_pkg,
                DRAM: c37_dram,
                'idle_intervals': get_idle_period_data(run, 'c37')
            },
            'hu-worker-c38': {
                PKG: c38_pkg,
                DRAM: c38_dram,
                'idle_intervals': get_idle_period_data(run, 'c38')
            },
        }

        # energy per task over execution
        package_energy_per_task = []
        dram_energy_per_task = []
        energy_per_task = []

        for index, row in run_df.iterrows():
            pkg = energy_by_host[row['hostname']][PKG].values.tolist()
            dram = energy_by_host[row['hostname']][DRAM].values.tolist()

            task_energy, task_dram = get_rapl_for_period(row['start'], row['complete'], pkg, dram)
            package_energy_per_task.append(task_energy)
            dram_energy_per_task.append(task_dram)
            energy_per_task.append(task_energy + task_dram)

        # overall energy per node over workflow execution
        package_energy_per_node = []
        dram_energy_per_node = []

        for hostname in energy_by_host.keys():
            pkg = energy_by_host[hostname][PKG].values.tolist()
            dram = energy_by_host[hostname][DRAM].values.tolist()

            node_energy, node_dram = get_rapl_for_period(workflow_start, workflow_end, pkg, dram)
            package_energy_per_node.append(node_energy)
            dram_energy_per_node.append(node_dram)

        # Overall Node Energy
        total_pkg_energy_per_node = sum(package_energy_per_node)
        total_dram_energy_per_node = sum(dram_energy_per_node)
        total_energy = total_pkg_energy_per_node + total_dram_energy_per_node
        total_pkg_kwh = convert_J_to_kWh(total_pkg_energy_per_node)
        total_dram_kwh = convert_J_to_kWh(total_dram_energy_per_node)
        total_kwh = convert_J_to_kWh(total_energy)

        print(workflow, 'run', run + 1)
        # print(total_pkg_energy_per_node, 'J', total_dram_energy_per_node, 'J', total_energy, 'J')
        print(total_pkg_kwh, 'kWh', total_dram_kwh, 'kWh', total_kwh, 'kWh')

        # idle energy
        package_idle_per_node = []
        dram_idle_per_node = []
        for hostname in energy_by_host.keys():
            pkg = energy_by_host[hostname][PKG].values.tolist()
            dram = energy_by_host[hostname][DRAM].values.tolist()
            idle_intervals = energy_by_host[hostname]['idle_intervals']

            for _, row in idle_intervals.iterrows():
                (task_energy, task_dram) = get_rapl_for_period(row['start_ms'], row['end_ms'], pkg, dram)
                package_idle_per_node.append(task_energy)
                dram_idle_per_node.append(task_dram)

        total_idle_pkg = convert_J_to_kWh(sum(package_idle_per_node))
        total_idle_dram = convert_J_to_kWh(sum(dram_idle_per_node))

        # Total - Idle Energy
        print('total - idle')
        print(total_pkg_kwh - total_idle_pkg, 'kWh', total_dram_kwh - total_idle_dram, 'kWh', total_kwh - total_idle_pkg - total_idle_dram, 'kWh')

        outfile.write(f'{run + 1},{total_pkg_kwh - total_idle_pkg},{total_dram_kwh - total_idle_dram},{total_kwh - total_idle_pkg - total_idle_dram}\n')
