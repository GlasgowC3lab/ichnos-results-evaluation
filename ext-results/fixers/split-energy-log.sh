# python convert-stamps.py rangeland/Run1/energy_log_c37.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_DRAM_log_c37.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_log_c38.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_DRAM_log_c38.txt 2025-10-15 2

# divide energy for 3 runs

python split-energy-log.py temp/1/c40_pkg.txt temp/1/stamp-1.csv c40 pkg
python split-energy-log.py temp/1/c40_dram.txt temp/1/stamp-1.csv c40 dram
python split-energy-log.py temp/1/c42_pkg.txt temp/1/stamp-1.csv c42 pkg
python split-energy-log.py temp/1/c42_dram.txt temp/1/stamp-1.csv c42 dram
python split-energy-log.py temp/1/c44_pkg.txt temp/1/stamp-1.csv c44 pkg
python split-energy-log.py temp/1/c44_dram.txt temp/1/stamp-1.csv c44 dram
python split-energy-log.py temp/1/c45_pkg.txt temp/1/stamp-1.csv c45 pkg
python split-energy-log.py temp/1/c45_dram.txt temp/1/stamp-1.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/1/trace

python split-energy-log.py temp/2/c40_pkg.txt temp/2/stamp-2.csv c40 pkg
python split-energy-log.py temp/2/c40_dram.txt temp/2/stamp-2.csv c40 dram
python split-energy-log.py temp/2/c42_pkg.txt temp/2/stamp-2.csv c42 pkg
python split-energy-log.py temp/2/c42_dram.txt temp/2/stamp-2.csv c42 dram
python split-energy-log.py temp/2/c44_pkg.txt temp/2/stamp-2.csv c44 pkg
python split-energy-log.py temp/2/c44_dram.txt temp/2/stamp-2.csv c44 dram
python split-energy-log.py temp/2/c45_pkg.txt temp/2/stamp-2.csv c45 pkg
python split-energy-log.py temp/2/c45_dram.txt temp/2/stamp-2.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/2/trace

python split-energy-log.py temp/3/c40_pkg.txt temp/3/stamp-3.csv c40 pkg
python split-energy-log.py temp/3/c40_dram.txt temp/3/stamp-3.csv c40 dram
python split-energy-log.py temp/3/c42_pkg.txt temp/3/stamp-3.csv c42 pkg
python split-energy-log.py temp/3/c42_dram.txt temp/3/stamp-3.csv c42 dram
python split-energy-log.py temp/3/c44_pkg.txt temp/3/stamp-3.csv c44 pkg
python split-energy-log.py temp/3/c44_dram.txt temp/3/stamp-3.csv c44 dram
python split-energy-log.py temp/3/c45_pkg.txt temp/3/stamp-3.csv c45 pkg
python split-energy-log.py temp/3/c45_dram.txt temp/3/stamp-3.csv c45 dram

python get_wf_periods.py ../aflow-experiments/high_cpu_high_mem/3/trace
