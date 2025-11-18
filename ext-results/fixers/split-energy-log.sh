# python convert-stamps.py rangeland/Run1/energy_log_c37.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_DRAM_log_c37.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_log_c38.txt 2025-10-15 2
# python convert-stamps.py rangeland/Run1/energy_DRAM_log_c38.txt 2025-10-15 2

# python convert-stamps.py rangeland/Run2/energy_log_c37.txt 2025-10-31 1
# python convert-stamps.py rangeland/Run2/energy_DRAM_log_c37.txt 2025-10-31 1
# python convert-stamps.py rangeland/Run2/energy_log_c38.txt 2025-10-31 1
# python convert-stamps.py rangeland/Run2/energy_DRAM_log_c38.txt 2025-10-31 1

# python convert-stamps.py sarek/Full_1/energy_log_c37.txt 2025-11-15 1
# python convert-stamps.py sarek/Full_1/energy_DRAM_log_c37.txt 2025-11-15 1
# python convert-stamps.py sarek/Full_1/energy_log_c38.txt 2025-11-15 1
# python convert-stamps.py sarek/Full_1/energy_DRAM_log_c38.txt 2025-11-15 1

# python convert-stamps.py sarek/Full_2/energy_log_c37.txt 2025-11-16 1
# python convert-stamps.py sarek/Full_2/energy_DRAM_log_c37.txt 2025-11-16 1
# python convert-stamps.py sarek/Full_2/energy_log_c38.txt 2025-11-16 1
# python convert-stamps.py sarek/Full_2/energy_DRAM_log_c38.txt 2025-11-16 1


# divide energy 

# data doesn't line up with the timestamp?
# python split-energy-log.py rangeland/Run1/conv-energy_log_c37.txt rangeland/Run1/stamps.csv c37 pkg
# python split-energy-log.py rangeland/Run1/conv-energy_DRAM_log_c37.txt rangeland/Run1/stamps.csv c37 dram
# python split-energy-log.py rangeland/Run1/conv-energy_log_c38.txt rangeland/Run1/stamps.csv c38 pkg
# python split-energy-log.py rangeland/Run1/conv-energy_DRAM_log_c38.txt rangeland/Run1/stamps.csv c38 dram

# python split-energy-log.py rangeland/Run2/conv-energy_log_c37.txt rangeland/Run2/stamps.csv c37 pkg
# python split-energy-log.py rangeland/Run2/conv-energy_DRAM_log_c37.txt rangeland/Run2/stamps.csv c37 dram
# python split-energy-log.py rangeland/Run2/conv-energy_log_c38.txt rangeland/Run2/stamps.csv c38 pkg
# python split-energy-log.py rangeland/Run2/conv-energy_DRAM_log_c38.txt rangeland/Run2/stamps.csv c38 dram

# python split-energy-log.py sarek/Full_1/conv-energy_log_c37.txt sarek/Full_1/stamps.csv c37 pkg
# python split-energy-log.py sarek/Full_1/conv-energy_DRAM_log_c37.txt sarek/Full_1/stamps.csv c37 dram
# python split-energy-log.py sarek/Full_1/conv-energy_log_c38.txt sarek/Full_1/stamps.csv c38 pkg
# python split-energy-log.py sarek/Full_1/conv-energy_DRAM_log_c38.txt sarek/Full_1/stamps.csv c38 dram

# python split-energy-log.py sarek/Full_2/conv-energy_log_c37.txt sarek/Full_2/stamps.csv c37 pkg
# python split-energy-log.py sarek/Full_2/conv-energy_DRAM_log_c37.txt sarek/Full_2/stamps.csv c37 dram
# python split-energy-log.py sarek/Full_2/conv-energy_log_c38.txt sarek/Full_2/stamps.csv c38 pkg
# python split-energy-log.py sarek/Full_2/conv-energy_DRAM_log_c38.txt sarek/Full_2/stamps.csv c38 dram
