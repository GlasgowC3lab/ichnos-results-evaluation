import sys


def read_memory_draw(node, gov, background=''):
    with open(f'memory/memory-{node}-{gov}{background}.csv', 'r') as f:
        lines = [line.strip().split(',') for line in f.readlines()[1:]]

    no_load_draw = float(lines[0][3])
    load_draw_avg = sum([float(line[3]) for line in lines[1:]]) / 10

    return (round(no_load_draw, 3), round(load_draw_avg, 3))



def write_output(all_data):
    filename = f'gu-mem-coeffs-bg.txt'

    with open(filename, 'w') as f:
        for node in all_data.keys():
            for gov in all_data[node].keys():
                no_load, load = all_data[node][gov]
                f.write(f'{node} + {gov}: load [{load}] no-load [{no_load}]\n')

    print(f'Model stored in file {filename}')


if __name__ == '__main__':
    total_mem = 256
    all_mem_coeffs = {}
    # nodes = ['huworkerc40', 'huworkerc42', 'huworkerc44', 'huworkerc45']
    nodes = ['gpgnode13', 'gpgnode14', 'gpgnode15', 'gpgnode16', 'gpgnode18']
    govs = ['ondemand']#, 'performance', 'powersave', 'schedutil']

    for node in nodes:
        all_mem_coeffs[node] = {}
        for gov in govs:
            all_mem_coeffs[node][gov] = {}
            mem_draw = read_memory_draw(node, gov, '-bg')
            all_mem_coeffs[node][gov] = mem_draw

    write_output(all_mem_coeffs)
