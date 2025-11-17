import sys
from datetime import datetime

HEADER_ROW = ',task_id,hash,native_id,process,tag,name,hostname,status,exit,module,container,cpus,time,disk,memory,attempt,submit,start,complete,duration,realtime,queue,%cpu,%mem,rss,vmem,peak_rss,peak_vmem,rchar,wchar,syscr,syscw,read_bytes,write_bytes,vol_ctxt,inv_ctxt,env,CPU_energy_consumption,DRAM_energy_consumption,energy_consumption,avg_power,cpu_model'


def parse_default_trace(filename):
    with open(f'{filename}.csv', 'r') as f:
        all = f.readlines()
        props = all[0].split(',')

    trace = []
    no_props = len(props)

    for line in all[1:]:
        temp = {}
        for val,idx in zip(line.split(','), range(0,no_props)):
            temp[props[idx].strip()] = val.strip()
        trace.append(temp)

    return trace


def convert_default_data(default):
    data = []

    for row in default:
        for prop in row.keys():
            if prop == 'submit' or prop == 'start' or prop == 'complete':
                value = convert_datetime(row[prop])
            elif prop == 'memory' or prop == 'peak_rss' or prop == 'peak_vmem': 
                value = convert_memory(row[prop])
            elif prop == 'realtime' or prop == 'time':
                value = convert_time(row[prop])
            elif prop == 'duration':
                value = int(float(row[prop]) * 1000)
            elif prop == '%mem':
                value = row[prop][:-1]
            else: 
                value = row[prop]

            row[prop] = str(value)

        data.append(','.join(row.values()) + ',' + 'Intel(R) Xeon(R) Silver 4314 CPU @ 2.40GHz')

    return data


def write_formatted_trace(filename, data):
    with open(filename, 'w') as f:
        f.write(HEADER_ROW + '\n')

        for row in data:
            f.write(row + '\n')


def convert_datetime(datetime_s):
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    date_obj = datetime.strptime(datetime_s, date_format)
    return int(date_obj.timestamp() * 1000)


def convert_time(time_s):
    parts = time_s.split(' ')
    no_parts = len(parts)

    if parts[0] == '-':
        return 0

    if no_parts == 1:
        if 'ms' in parts[-1]:
            return float(parts[-1][:-2])
        else:
            secs = float(parts[-1][:-1])
            mins = 0
            hours = 0
    elif no_parts == 2:
        secs = float(parts[-1][:-1])
        mins = int(parts[-2][:-1])
        hours = 0
    elif no_parts == 3:
        secs = float(parts[-1][:-1])
        mins = int(parts[-2][:-1])
        hours = int(parts[-3][:-1])
    else:
        secs = 0
        mins = 0
        hours = 0

    converted = secs + (mins * 60) + (hours * 60 * 60)

    return int(converted * 1000)


def convert_memory(memory_s):
    parts = memory_s.strip().split(' ')

    if parts[0] == '' or parts[0] == '-':
        return 0
    elif len(parts) == 1:
        return parts[0]
    else:
        value = float(parts[0])
        unit = parts[1]

        if unit == 'KB':
            return value * 1024
        elif unit == 'MB':
            return value * 1024 * 1024
        elif unit == 'GB':
            return value * 1024 * 1024 * 1024
        elif unit == 'TB':
            return value * 1024 * 1024 * 1024 * 1024
        else:
            return value


if __name__ == '__main__':
    args = sys.argv[1:]
    filename = args[0]
    out_filename = 'out/' + args[1] + '.csv'

    print(f'Default Trace: {filename}')

    default = parse_default_trace(filename)
    data = convert_default_data(default)
    write_formatted_trace(out_filename, data)

    print(f'Formatted Trace: {out_filename}')
