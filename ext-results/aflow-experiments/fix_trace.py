import sys
import pandas as pd


def load_and_adjust(experiment, iteration, model):
    trace_file = f'{experiment}/{iteration}/trace.csv'
    df = pd.read_csv(trace_file, header=0)
    df['cpu_model'] = model
    df.to_csv(trace_file)


# Main Script
args = sys.argv[1:]
experiment = args[0]
model = 'Intel Xeon Silver 4314'  # used for all experiments

for run in range(1, 4):
    load_and_adjust(experiment, run, model)
