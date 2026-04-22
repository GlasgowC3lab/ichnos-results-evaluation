import sys
import csv
from pathlib import Path

def main(args):
    energy_file = Path(args[1])
    run_file = Path(args[2])

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
        lines = [line.strip() for line in f if line.strip()]

    readings = []
    for i in range(0, len(lines), 3):  # for gpg nodes
    # for i in range(0, len(lines), 2):
        if i + 2 < len(lines):  # for gpg nodes
        # if i + 1 < len(lines):
            try:
                energy_1 = lines[i]
                energy_2 = lines[i+1]  # for gpg nodes
                ts = int(lines[i + 2])  # for gpg nodes
                # ts = int(lines[i + 1])
                readings.append((ts, energy_1, energy_2))  # for gpg nodes
                # readings.append((ts, energy_1))
            except ValueError:
                continue

    # assign readings
    for ts, energy_1, energy_2 in readings:  #for gpg nodes
    # for ts, energy_1 in readings:
        for run in runs:
            if run["start"] < ts < run["end"]:
                run["data"].append((ts, energy_1, energy_2))
                # run["data"].append((ts, energy_1))
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
    if len(sys.argv) != 5:
        print("Usage: python split_energy_by_run.py <energy_file.txt> <run-stamps.csv> <node> <pkg|dram>")
        sys.exit(1)

    main(sys.argv)
