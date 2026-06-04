import numpy as np
import sys


def read_ts(filename):
    ts_data = {}

    with open(filename, 'r') as f:
        data = f.readlines()

    for load, row_i in zip(range(0, 100, 10), range(1,12)):
        ts_data[load] = float(data[row_i].strip().split(',')[3])

    ts_data[100] = float(data[14].strip().split(',')[3])  # power consumption with maximize stress test

    mem_idle = float(data[1].strip().split(',')[4])
    mem_max = float(data[13].strip().split(',')[4])  # memory power consumption with VMStress stress test

    return (ts_data, (mem_idle, mem_max))

def get_average_ts_files(path):
    paths = [path.replace('ITER', str(iteration)) for iteration in range(1, 4)]
    readings = {}
    mem_readings = []

    for path in paths:
        (path_data, mem_data) = read_ts(path)

        for load,val in path_data.items():
            if load in readings:
                readings[load].append(val)
            else:
                readings[load] = [val]

        avg_mem_draw = (mem_data[0] + mem_data[1]) / 2
        mem_readings.append(avg_mem_draw)

    data = {}

    for load,vals in readings.items():
        data[load] = sum(vals) / 3

    overall_avg_mem_draw = sum(mem_readings) / 3

    return (data, overall_avg_mem_draw)

class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def __str__(self):
        chunks = []
        for coeff in self.coeffs:
            if coeff == 0:
                continue
            chunks.append(self.format_coeff(coeff))
        return f"[ {', '.join(chunks)} ]"

    @staticmethod
    def format_coeff(coeff):
        return str(coeff)

    @staticmethod
    def format_power(power):
        return str(power) if power > 1 else ''


# Helper Functions
def make_model(node, governor, background=False):
    if background:
        ts_path = f'{node}-bg/ts-{node.replace('-', '')}-{governor}-ITER.csv'
    else:
        ts_path = f'{node}/ts-ITER.csv'
    node_stats = {}
    (node_stats[node], mem_draw) = get_average_ts_files(ts_path)
    x = range(0,110,10)
    y = node_stats[node].values()
    y_arr = list(y)

    linear_v2_coef = np.polyfit(x, y_arr, 1)
    linear_v2 = np.poly1d(linear_v2_coef)
    model_linear_v2 = Polynomial(linear_v2)

    return (model_linear_v2, mem_draw, (min(y_arr), max(y_arr)))


# update to store in the format expected by ichnos / JSON ? or easily parseable record
# add versioning, i.e. date/timestamp for it, version like 1.0 and then increment -> 1.1 -- 1.11+
def write_output(node, governor, model):
    filename = f'models/{governor}-{node}-bg-model.txt'

    with open(filename, 'w') as f:
        model_str = str(model)
        f.write(filename + '\n')
        f.write(model_str + '\n')


if __name__ == '__main__':
    args = sys.argv[1:]
    node = args[0].strip()
    governor = args[1].strip()
    background = bool(args[2].strip())
    (model, mem_draw, minmax) = make_model(node, governor, background)
    write_output(node, governor, model)
