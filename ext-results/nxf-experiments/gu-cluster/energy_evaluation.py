import sys
import pandas as pd


# Constants
rapl_max_value_overflow = 65532610987
rapl_DRAM_max_value_overflow = 65532610987
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
    pkg_df['energy_1'] = pkg_df['energy_1'].astype(float)
    pkg_df['energy_2'] = pkg_df['energy_2'].astype(float)

    with open(dram_file) as file:
        stripped_lines = [line.rstrip().split(',') for line in file.readlines()]
        dram_data = stripped_lines[1:]

    dram_df = pd.DataFrame(dram_data, columns=header)
    dram_df['timestamp'] = dram_df['timestamp'].astype(int)
    dram_df['energy_1'] = dram_df['energy_1'].astype(float)
    dram_df['energy_2'] = dram_df['energy_2'].astype(float)

    return pkg_df, dram_df


def convert_J_to_kWh(joules):
    return joules / 3600000


def get_rapl_for_period(start_time, end_time, package_log, dram_log):
    calculated_consumption = False 
    position = 0
    start_point_found = False
    energy_consumed_1 = 0
    energy_consumed_2 = 0
    start_energy_1 = 0
    start_energy_2 = 0
    overflows_1 = 0
    overflows_2 = 0

    while not calculated_consumption and position < len(package_log):
        if not start_point_found:
            if start_time <= package_log[position][0]:
                start_point_found = True
                start_energy_1 = package_log[position][1]
                start_energy_2 = package_log[position][2]
                position = position - 1
        else:
            if package_log[position][1] < package_log[position - 1][1]:
                overflows_1 += 1
            if package_log[position][2] < package_log[position - 1][2]:
                overflows_2 += 2
            if end_time <= package_log[position][0]: 
                energy_consumed_1 = (package_log[position][1] + (overflows_1 * rapl_max_value_overflow) - start_energy_1) * energy_unit_joules
                energy_consumed_2 = (package_log[position][2] + (overflows_2 * rapl_max_value_overflow) - start_energy_2) * energy_unit_joules
                calculated_consumption = True
        position += 1

    if not calculated_consumption:
        energy_consumed_1 = (package_log[-1][1] + (overflows_1 * rapl_max_value_overflow) - start_energy_1) * energy_unit_joules
        energy_consumed_2 = (package_log[-1][2] + (overflows_2 * rapl_max_value_overflow) - start_energy_2) * energy_unit_joules

    calculated_consumption = False 
    position = 0
    start_point_found = False
    dram_energy_consumed_1 = 0
    dram_energy_consumed_2 = 0
    start_energy_1 = 0
    start_energy_2 = 0
    overflows_1 = 0
    overflows_2 = 0

    while not calculated_consumption and position < len(dram_log):
        if not start_point_found:
            if start_time <= dram_log[position][0]:
                start_point_found = True
                start_energy_1 = dram_log[position][1]
                start_energy_2 = dram_log[position][2]
                position = position - 1
        else:
            if dram_log[position][1] < dram_log[position - 1][1]:
                overflows_1 += 1
            if dram_log[position][2] < dram_log[position - 1][2]:
                overflows_2 += 1
            if end_time <= dram_log[position][0]: 
                dram_energy_consumed_1 = (dram_log[position][1] + (overflows_1 * rapl_DRAM_max_value_overflow) - start_energy_1) * energy_unit_joules
                dram_energy_consumed_2 = (dram_log[position][2] + (overflows_2 * rapl_DRAM_max_value_overflow) - start_energy_2) * energy_unit_joules
                calculated_consumption = True
        position += 1

    if not calculated_consumption:
        dram_energy_consumed_1 = (dram_log[-1][1] + (overflows_1 * rapl_DRAM_max_value_overflow) - start_energy_1) * energy_unit_joules
        dram_energy_consumed_2 = (dram_log[-1][1] + (overflows_2 * rapl_DRAM_max_value_overflow) - start_energy_2) * energy_unit_joules

    return ((energy_consumed_1, energy_consumed_2), (dram_energy_consumed_1, dram_energy_consumed_2))

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

with open(f'{workflow}-runs.csv', 'w') as outfile:
    outfile.write('run,pkg,dram,total\n')

    for run in range(0, runs): 
        task_data = []
        trace = f'{workflow}/{run+1}/trace.csv'
        energy_dir = f'{workflow}/{run+1}/energy/'
        pkg_gpg12 = energy_dir + f'run_{run+1}_gpgnode12_pkg.csv'
        #pkg_gpg13 = energy_dir + f'run_{run+1}_gpgnode13_pkg.csv'
        pkg_gpg14 = energy_dir + f'run_{run+1}_gpgnode14_pkg.csv'
        pkg_gpg15 = energy_dir + f'run_{run+1}_gpgnode15_pkg.csv'
        pkg_gpg16 = energy_dir + f'run_{run+1}_gpgnode16_pkg.csv'
        pkg_gpg17 = energy_dir + f'run_{run+1}_gpgnode17_pkg.csv'
        pkg_gpg18 = energy_dir + f'run_{run+1}_gpgnode18_pkg.csv'
        pkg_gpg19 = energy_dir + f'run_{run+1}_gpgnode19_pkg.csv'
        dram_gpg12 = energy_dir + f'run_{run+1}_gpgnode12_dram.csv'
        #dram_gpg13 = energy_dir + f'run_{run+1}_gpgnode13_dram.csv'
        dram_gpg14 = energy_dir + f'run_{run+1}_gpgnode14_dram.csv'
        dram_gpg15 = energy_dir + f'run_{run+1}_gpgnode15_dram.csv'
        dram_gpg16 = energy_dir + f'run_{run+1}_gpgnode16_dram.csv'
        dram_gpg17 = energy_dir + f'run_{run+1}_gpgnode17_dram.csv'
        dram_gpg18 = energy_dir + f'run_{run+1}_gpgnode18_dram.csv'
        dram_gpg19 = energy_dir + f'run_{run+1}_gpgnode19_dram.csv'

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
        gpg12_pkg, gpg12_dram = get_energy_data(pkg_gpg12, dram_gpg12)
        #gpg13_pkg, gpg13_dram = get_energy_data(pkg_gpg13, dram_gpg13)
        gpg14_pkg, gpg14_dram = get_energy_data(pkg_gpg14, dram_gpg14)
        gpg15_pkg, gpg15_dram = get_energy_data(pkg_gpg15, dram_gpg15)
        gpg16_pkg, gpg16_dram = get_energy_data(pkg_gpg16, dram_gpg16)
        gpg17_pkg, gpg17_dram = get_energy_data(pkg_gpg17, dram_gpg17)
        gpg18_pkg, gpg18_dram = get_energy_data(pkg_gpg18, dram_gpg18)
        gpg19_pkg, gpg19_dram = get_energy_data(pkg_gpg19, dram_gpg19)
        energy_by_host = {
            'gpgnode-12': {
                PKG: gpg12_pkg,
                DRAM: gpg12_dram,
                'idle_intervals': get_idle_period_data(run, '12')
            },
            'gpgnode-14': {
                PKG: gpg14_pkg,
                DRAM: gpg14_dram,
                'idle_intervals': get_idle_period_data(run, '14')
            },
            'gpgnode-15': {
                PKG: gpg15_pkg,
                DRAM: gpg15_dram,
                'idle_intervals': get_idle_period_data(run, '15')
            },
            'gpgnode-16': {
                PKG: gpg16_pkg,
                DRAM: gpg16_dram,
                'idle_intervals': get_idle_period_data(run, '16')
            },
            'gpgnode-17': {
                PKG: gpg17_pkg,
                DRAM: gpg17_dram,
                'idle_intervals': get_idle_period_data(run, '17')
            },
            'gpgnode-18': {
                PKG: gpg18_pkg,
                DRAM: gpg18_dram,
                'idle_intervals': get_idle_period_data(run, '18')
            },
            'gpgnode-19': {
                PKG: gpg19_pkg,
                DRAM: gpg19_dram,
                'idle_intervals': get_idle_period_data(run, '19')
            },
        }

        # energy per task over execution
        package_energy_per_task = []
        dram_energy_per_task = []
        energy_per_task = []

        for index, row in run_df.iterrows():
            pkg = energy_by_host[row['hostname']][PKG].values.tolist()
            dram = energy_by_host[row['hostname']][DRAM].values.tolist()

            (task_energy_1, task_energy_2), (task_dram_1, task_dram_2) = get_rapl_for_period(row['start'], row['complete'], pkg, dram)
            package_energy_per_task.append(task_energy_1 + task_energy_2)
            dram_energy_per_task.append(task_dram_1 + task_dram_2)
            energy_per_task.append(task_energy_1 + task_energy_2 + task_dram_1 + task_dram_2)

        # idle energy
        package_idle_per_node = []
        dram_idle_per_node = []
        for hostname in energy_by_host.keys():
            pkg = energy_by_host[hostname][PKG].values.tolist()
            dram = energy_by_host[hostname][DRAM].values.tolist()
            idle_intervals = energy_by_host[hostname]['idle_intervals']

            for _, row in idle_intervals.iterrows():
                (task_energy_1, task_energy_2), (task_dram_1, task_dram_2) = get_rapl_for_period(row['start_ms'], row['end_ms'], pkg, dram)
                package_idle_per_node.append(task_energy_1 + task_energy_2)
                dram_idle_per_node.append(task_dram_1 + task_dram_2)

        total_idle_pkg = sum(package_idle_per_node)
        total_idle_dram = sum(dram_idle_per_node)

        # overall energy per node over workflow execution
        package_energy_per_node_1 = []
        dram_energy_per_node_1 = []
        package_energy_per_node_2 = []
        dram_energy_per_node_2 = []

        for hostname in energy_by_host.keys():
            pkg = energy_by_host[hostname][PKG].values.tolist()
            dram = energy_by_host[hostname][DRAM].values.tolist()

            (node_energy_1, node_energy_2), (node_dram_1, node_dram_2) = get_rapl_for_period(workflow_start, workflow_end, pkg, dram)
            package_energy_per_node_1.append(node_energy_1)
            dram_energy_per_node_1.append(node_dram_1)
            package_energy_per_node_2.append(node_energy_2)
            dram_energy_per_node_2.append(node_dram_2)

        # Overall Node Energy
        total_pkg_energy_per_node_1 = sum(package_energy_per_node_1)
        total_dram_energy_per_node_1 = sum(dram_energy_per_node_1)
        total_energy_1 = total_pkg_energy_per_node_1 + total_dram_energy_per_node_1
        total_pkg_kwh_1 = convert_J_to_kWh(total_pkg_energy_per_node_1)
        total_dram_kwh_1 = convert_J_to_kWh(total_dram_energy_per_node_1)
        total_kwh_1 = convert_J_to_kWh(total_energy_1)

        total_pkg_energy_per_node_2 = sum(package_energy_per_node_2)
        total_dram_energy_per_node_2 = sum(dram_energy_per_node_2)
        total_energy_2 = total_pkg_energy_per_node_2 + total_dram_energy_per_node_2
        total_pkg_kwh_2 = convert_J_to_kWh(total_pkg_energy_per_node_2)
        total_dram_kwh_2 = convert_J_to_kWh(total_dram_energy_per_node_2)
        total_kwh_2 = convert_J_to_kWh(total_energy_2)

        print(workflow, 'run', run + 1)
        # print(total_pkg_energy_per_node, 'J', total_dram_energy_per_node, 'J', total_energy, 'J')
        #print(total_pkg_kwh_1, 'kWh', total_dram_kwh_1, 'kWh', total_kwh_1, 'kWh')
        #print(total_pkg_kwh_2, 'kWh', total_dram_kwh_2, 'kWh', total_kwh_2, 'kWh')
        print('overall')
        print(total_pkg_kwh_1+total_pkg_kwh_2, 'kWh', 
            total_dram_kwh_1+total_dram_kwh_2, 'kWh', 
            total_kwh_1+total_kwh_2, 'kWh')

        print('idle')
        pkg_idle_kwh = convert_J_to_kWh(total_idle_pkg)
        dram_idle_kwh = convert_J_to_kWh(total_idle_dram)
        print(pkg_idle_kwh, 'kWh', dram_idle_kwh, 'kWh', pkg_idle_kwh + dram_idle_kwh, 'kWh')

        print('actual')
        print(total_pkg_kwh_1 + total_pkg_kwh_2 - pkg_idle_kwh, 'kWh', 
            total_dram_kwh_1 + total_dram_kwh_2 - dram_idle_kwh, 'kWh', 
            total_kwh_1 + total_kwh_2 - pkg_idle_kwh - dram_idle_kwh, 'kWh')

        outfile.write(f"{run+1},{total_pkg_kwh_1 + total_pkg_kwh_2 - pkg_idle_kwh},{total_dram_kwh_1 + total_dram_kwh_2 - dram_idle_kwh},{ 
            total_kwh_1 + total_kwh_2 - pkg_idle_kwh - dram_idle_kwh}\n")
