# divide energy for 3 runs

python split-energy-log.py temp/low_cpu_low_mem/1/logs/c40_pkg.txt temp/low_cpu_low_mem/1/stamp-1.csv c40 pkg
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c40_dram.txt temp/low_cpu_low_mem/1/stamp-1.csv c40 dram
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c42_pkg.txt temp/low_cpu_low_mem/1/stamp-1.csv c42 pkg
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c42_dram.txt temp/low_cpu_low_mem/1/stamp-1.csv c42 dram
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c44_pkg.txt temp/low_cpu_low_mem/1/stamp-1.csv c44 pkg
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c44_dram.txt temp/low_cpu_low_mem/1/stamp-1.csv c44 dram
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c45_pkg.txt temp/low_cpu_low_mem/1/stamp-1.csv c45 pkg
python split-energy-log.py temp/low_cpu_low_mem/1/logs/c45_dram.txt temp/low_cpu_low_mem/1/stamp-1.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/1/trace

python split-energy-log.py temp/low_cpu_low_mem/2/logs/c40_pkg.txt temp/low_cpu_low_mem/2/stamp-2.csv c40 pkg
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c40_dram.txt temp/low_cpu_low_mem/2/stamp-2.csv c40 dram
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c42_pkg.txt temp/low_cpu_low_mem/2/stamp-2.csv c42 pkg
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c42_dram.txt temp/low_cpu_low_mem/2/stamp-2.csv c42 dram
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c44_pkg.txt temp/low_cpu_low_mem/2/stamp-2.csv c44 pkg
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c44_dram.txt temp/low_cpu_low_mem/2/stamp-2.csv c44 dram
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c45_pkg.txt temp/low_cpu_low_mem/2/stamp-2.csv c45 pkg
python split-energy-log.py temp/low_cpu_low_mem/2/logs/c45_dram.txt temp/low_cpu_low_mem/2/stamp-2.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/2/trace

python split-energy-log.py temp/low_cpu_low_mem/3/logs/c40_pkg.txt temp/low_cpu_low_mem/3/stamp-3.csv c40 pkg
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c40_dram.txt temp/low_cpu_low_mem/3/stamp-3.csv c40 dram
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c42_pkg.txt temp/low_cpu_low_mem/3/stamp-3.csv c42 pkg
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c42_dram.txt temp/low_cpu_low_mem/3/stamp-3.csv c42 dram
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c44_pkg.txt temp/low_cpu_low_mem/3/stamp-3.csv c44 pkg
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c44_dram.txt temp/low_cpu_low_mem/3/stamp-3.csv c44 dram
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c45_pkg.txt temp/low_cpu_low_mem/3/stamp-3.csv c45 pkg
python split-energy-log.py temp/low_cpu_low_mem/3/logs/c45_dram.txt temp/low_cpu_low_mem/3/stamp-3.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/3/trace
