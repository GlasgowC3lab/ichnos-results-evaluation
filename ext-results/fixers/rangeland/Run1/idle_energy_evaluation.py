import sys
import re
import os
import seaborn as sns
import pandas as pd
from datetime import datetime
from datetime import timedelta
#import datetime
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from scipy.stats import pearsonr
import plotly.graph_objects as go

rapl_max_value_overflow = 262143328850
rapl_DRAM_max_value_overflow = 65712999613

script_dir = os.path.dirname(os.path.abspath(__file__))

rapl_measurements1 = os.path.join(script_dir, "energy_log_c37.txt")
rapl_measurements2 = os.path.join(script_dir, "energy_log_c38.txt")
DRAM_measurements1 = os.path.join(script_dir, "energy_DRAM_log_c37.txt")
DRAM_measurements2 = os.path.join(script_dir, "energy_DRAM_log_c38.txt")

#read rapl measurements (node 37)
with open(rapl_measurements1) as file:
    measurements = [line.rstrip() for line in file]

rapl_raw = []
time_points = []
rapl_with_time1 = []

for i in range(len(measurements)):
    if (i % 2 == 0):
        rapl_raw.append(int(measurements[i]))
    if (i % 2 == 1):
        time_points.append(datetime.strptime(measurements[i][0:8], "%H:%M:%S"))

for j in range(len(rapl_raw)):
    rapl_with_time1.append((rapl_raw[j], time_points[j]))

#read rapl measurements (node 38)
with open(rapl_measurements2) as file:
    measurements = [line.rstrip() for line in file]

rapl_raw = []
time_points = []
rapl_with_time2 = []

for i in range(len(measurements)):
    if (i % 2 == 0):
        rapl_raw.append(int(measurements[i]))
    if (i % 2 == 1):
        time_points.append(datetime.strptime(measurements[i][0:8], "%H:%M:%S"))

for j in range(len(rapl_raw)):
    rapl_with_time2.append((rapl_raw[j], time_points[j]))


#read DRAM measurements (node 37)
with open(DRAM_measurements1) as file:
    measurements = [line.rstrip() for line in file]

rapl_raw = []
time_points = []
DRAM_with_time1 = []

for i in range(len(measurements)):
    if (i % 2 == 0):
        rapl_raw.append(int(measurements[i]))
    if (i % 2 == 1):
        time_points.append(datetime.strptime(measurements[i][0:8], "%H:%M:%S"))

for j in range(len(rapl_raw)):
    DRAM_with_time1.append((rapl_raw[j], time_points[j]))


#read DRAM measurements (node 38)
with open(DRAM_measurements2) as file:
    measurements = [line.rstrip() for line in file]

rapl_raw = []
time_points = []
DRAM_with_time2 = []

for i in range(len(measurements)):
    if (i % 2 == 0):
        rapl_raw.append(int(measurements[i]))
    if (i % 2 == 1):
        time_points.append(datetime.strptime(measurements[i][0:8], "%H:%M:%S"))

for j in range(len(rapl_raw)):
    DRAM_with_time2.append((rapl_raw[j], time_points[j]))

energy_unit_joules = 15.3e-7

overflows = 0
for x in range(len(rapl_with_time1) - 1):  # -1 to avoid index out of range
    if rapl_with_time1[x][0] > rapl_with_time1[x + 1][0]:
        overflows += 1
energy_consumed_rapl1 = (rapl_with_time1[-1][0] + (overflows * rapl_max_value_overflow) - rapl_with_time1[0][0]) * energy_unit_joules

overflows = 0
for x in range(len(rapl_with_time2) - 1):  # -1 to avoid index out of range
    if rapl_with_time2[x][0] > rapl_with_time2[x + 1][0]:
        overflows += 1
energy_consumed_rapl2 = (rapl_with_time2[-1][0] + (overflows * rapl_max_value_overflow) - rapl_with_time2[0][0]) * energy_unit_joules

overflows = 0
for x in range(len(DRAM_with_time1) - 1):  # -1 to avoid index out of range
    if DRAM_with_time1[x][0] > DRAM_with_time1[x + 1][0]:
        overflows += 1
energy_consumed_DRAM1 = (DRAM_with_time1[-1][0] + (overflows * rapl_DRAM_max_value_overflow) - DRAM_with_time1[0][0]) * energy_unit_joules

overflows = 0
for x in range(len(DRAM_with_time2) - 1):  # -1 to avoid index out of range
    if DRAM_with_time2[x][0] > DRAM_with_time2[x + 1][0]:
        overflows += 1
energy_consumed_DRAM2 = (DRAM_with_time2[-1][0] + (overflows * rapl_DRAM_max_value_overflow) - DRAM_with_time2[0][0]) * energy_unit_joules

energy_consumed_total = energy_consumed_rapl1 + energy_consumed_rapl2 + energy_consumed_DRAM1 + energy_consumed_DRAM2

print(f"Energy consumed by RAPL1: {energy_consumed_rapl1:.2f} Joules")
print(f"Energy consumed by RAPL2: {energy_consumed_rapl2:.2f} Joules")
print(f"Energy consumed by DRAM1: {energy_consumed_DRAM1:.2f} Joules")
print(f"Energy consumed by DRAM2: {energy_consumed_DRAM2:.2f} Joules")
print(f"Total energy consumed: {energy_consumed_total:.2f} Joules")
