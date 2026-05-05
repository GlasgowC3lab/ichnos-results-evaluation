import sys
import csv
from pathlib import Path

def main(args):
    energy_file = Path(args[1])
    run_file = Path(args[2])
    backup_energy_file = Path(args[5])

    # read runs
    runs = []
    with open(run_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                runs.append({
                    "run": int(row["run"]),
                    "start": int(row["start"]),
                    "end": int(row["end"]),
                    "data": []  
                })
            except ValueError:
                continue

    with open(energy_file) as f:
        val_lines = [line.strip() for line in f if line.strip()]

    ts_lines = []
    odd = True
    with open(backup_energy_file) as f:
        for line in f.readlines()[1:]:
            if line.strip():
                if odd:
                    ts_lines.append(line.strip())
                    odd = False
                else:
                    odd = True

    readings = []
    for i in range(0, len(val_lines)):
        tss = int(ts_lines[i])
        val = val_lines[i]
        readings.append((tss, val))

    # assign readings
    for ts, energy_1 in readings:
        for run in runs:
            if run["start"] < ts < run["end"]:
                run["data"].append((ts, energy_1))
                break  

    # write output
    for run in runs:
        out_file = f"run_{run['run']}_{args[3]}_{args[4]}.csv"
        with open(out_file, "w", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["timestamp", "energy"])
            writer.writerows(run["data"])

"""
Split energy readings into separate CSVs per run based on start/end times.

Usage:
    python split_energy_by_run.py energy_file.txt run-stamps.csv
"""
if __name__ == "__main__":
    main(sys.argv)
