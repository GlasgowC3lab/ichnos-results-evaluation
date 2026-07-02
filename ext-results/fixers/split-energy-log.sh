# divide energy for 3 runs

python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c40_pkg.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c40 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c40_dram.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c40 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c42_pkg.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c42 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c42_dram.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c42 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c44_pkg.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c44 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c44_dram.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c44 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c45_pkg.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c45 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/1/logs/c45_dram.txt temp/ichnos_low_cpu_low_mem/1/stamp-1.csv c45 dram

python3 get_wf_periods.py temp/ichnos_low_cpu_low_mem/1/trace
mkdir temp/ichnos_low_cpu_low_mem/1/energy/
mv period_exports/* temp/ichnos_low_cpu_low_mem/1/energy/
mv run_1_*.csv temp/ichnos_low_cpu_low_mem/1/energy/

python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c40_pkg.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c40 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c40_dram.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c40 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c42_pkg.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c42 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c42_dram.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c42 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c44_pkg.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c44 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c44_dram.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c44 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c45_pkg.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c45 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/2/logs/c45_dram.txt temp/ichnos_low_cpu_low_mem/2/stamp-2.csv c45 dram

python3 get_wf_periods.py temp/ichnos_low_cpu_low_mem/2/trace
mkdir temp/ichnos_low_cpu_low_mem/2/energy/
mv period_exports/* temp/ichnos_low_cpu_low_mem/2/energy/
mv run_2_*.csv temp/ichnos_low_cpu_low_mem/2/energy/

python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c40_pkg.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c40 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c40_dram.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c40 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c42_pkg.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c42 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c42_dram.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c42 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c44_pkg.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c44 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c44_dram.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c44 dram
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c45_pkg.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c45 pkg
python3 split-energy-log.py temp/ichnos_low_cpu_low_mem/3/logs/c45_dram.txt temp/ichnos_low_cpu_low_mem/3/stamp-3.csv c45 dram

python3 get_wf_periods.py temp/ichnos_low_cpu_low_mem/3/trace
mkdir temp/ichnos_low_cpu_low_mem/3/energy/
mv period_exports/* temp/ichnos_low_cpu_low_mem/3/energy/
mv run_3_*.csv temp/ichnos_low_cpu_low_mem/3/energy/
