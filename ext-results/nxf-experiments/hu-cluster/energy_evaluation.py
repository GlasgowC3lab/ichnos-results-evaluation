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


def get_active_period_data(run, node):
    energy_dir = f'{workflow}/{run+1}/energy/'
    with open(energy_dir + f'active_{node}.csv') as file:
        stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
        header = stripped_lines[0]
        data = stripped_lines[1:]

    active_periods = pd.DataFrame(data, columns=header).drop(columns=['start_time', 'end_time'])
    active_periods['start_ms'] = active_periods['start_ms'].astype(float)
    active_periods['end_ms'] = active_periods['end_ms'].astype(float)
    return active_periods


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
    outfile.write('run,pkg,dram,total,idle_pkg,idle_dram,idle_total,active_pkg,active_dram,active_total\n')

    for run in range(0, runs): 
        task_data = []
        trace = f'{workflow}/{run+1}/trace.csv'
        energy_dir = f'{workflow}/{run+1}/energy/'
        pkg_c40 = energy_dir + f'run_{run+1}_c40_pkg.csv'
        pkg_c42 = energy_dir + f'run_{run+1}_c42_pkg.csv'
        pkg_c44 = energy_dir + f'run_{run+1}_c44_pkg.csv'
        pkg_c45 = energy_dir + f'run_{run+1}_c45_pkg.csv'
        dram_c40 = energy_dir + f'run_{run+1}_c40_dram.csv'
        dram_c42 = energy_dir + f'run_{run+1}_c42_dram.csv'
        dram_c44 = energy_dir + f'run_{run+1}_c44_dram.csv'
        dram_c45 = energy_dir + f'run_{run+1}_c45_dram.csv'

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
        c40_pkg, c40_dram = get_energy_data(pkg_c40, dram_c40)
        c42_pkg, c42_dram = get_energy_data(pkg_c42, dram_c42)
        c44_pkg, c44_dram = get_energy_data(pkg_c44, dram_c44)
        c45_pkg, c45_dram = get_energy_data(pkg_c45, dram_c45)
        energy_by_host = {
            'hu-worker-c40': {
                PKG: c40_pkg,
                DRAM: c40_dram,
                'idle_intervals': get_idle_period_data(run, 'c40'),
                'active_intervals': get_active_period_data(run, 'c40')
            },
            'hu-worker-c42': {
                PKG: c42_pkg,
                DRAM: c42_dram,
                'idle_intervals': get_idle_period_data(run, 'c42'),
                'active_intervals': get_active_period_data(run, 'c42')
            },
            'hu-worker-c44': {
                PKG: c44_pkg,
                DRAM: c44_dram,
                'idle_intervals': get_idle_period_data(run, 'c44'),
                'active_intervals': get_active_period_data(run, 'c44')
            },
            'hu-worker-c45': {
                PKG: c45_pkg,
                DRAM: c45_dram,
                'idle_intervals': get_idle_period_data(run, 'c45'),
                'active_intervals': get_active_period_data(run, 'c45')
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

        # active energy
        package_active_per_node = []
        dram_active_per_node = []
        for hostname in energy_by_host.keys():
            pkg = energy_by_host[hostname][PKG].values.tolist()
            dram = energy_by_host[hostname][DRAM].values.tolist()
            active_intervals = energy_by_host[hostname]['active_intervals']

            for _, row in active_intervals.iterrows():
                (task_energy, task_dram) = get_rapl_for_period(row['start_ms'], row['end_ms'], pkg, dram)
                package_active_per_node.append(task_energy)
                dram_active_per_node.append(task_dram)

        total_active_pkg = convert_J_to_kWh(sum(package_active_per_node))
        total_active_dram = convert_J_to_kWh(sum(dram_active_per_node))

        # if total_dram_kwh < 0:
        #     total_dram_kwh *= -1  # make positive
        #     total_dram_kwh = abs(total_dram_kwh - total_idle_dram)
        # else:
        #     total_dram_kwh = total_dram_kwh - total_idle_dram

        # total_kwh = total_pkg_kwh - total_idle_pkg

        # Report on Energy
        outfile.write(f'{run + 1},{total_pkg_kwh},{total_dram_kwh},{total_kwh},\
{total_idle_pkg},{total_idle_dram},{total_idle_pkg + total_idle_dram},\
{total_active_pkg},{total_active_dram},{total_active_pkg + total_active_dram}\n')
