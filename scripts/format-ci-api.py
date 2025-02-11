# Imports
import sys


# Constants
FILE = 'file'
OUT_FILE = 'file-out'
REGION_LOC = 2


# Functions
def parse_arguments(args):
    if len(args) != 2:
        print("Expected Usage: python -m scripts.format-ci-api <source-filename> <formatted-filename")

    return {FILE: args[0].strip(), OUT_FILE: args[1]}


def get_end(start):
    parts = start.split(':')

    if start == "23:30":
        hours = "00"
        mins = "00"
    elif int(parts[1]) == 30:
        mins = "00"
        hours = str(int(parts[0]) + 1).zfill(2)
    else:
        mins = "30"
        hours = parts[0]

    return f"{hours}:{mins}"


def parse_data(filename):
    with open(f'data/intensity/{filename}', 'r') as f:
        raw = f.readlines()

    data = []

    for entry in raw[2:]:
        parts = entry.split(',')
        date_parts = parts[0].split('T')
        date = date_parts[0]
        start = date_parts[1][:-1]
        end = get_end(start)
        value = float(parts[REGION_LOC])
        data.append([date, start, end, str(value)])

    return data


def write_data(output_filename, records):
    with open(f"data/intensity/{output_filename}", "w") as f:
        f.write("date,start,end,actual\n")

        for record in records:
            f.write(",".join(record) + "\n")


# Main
if __name__ == '__main__':
    args = sys.argv[1:]
    settings = parse_arguments(args)

    filename = settings[FILE]
    output_filename = settings[OUT_FILE]
    data = parse_data(filename)
    write_data(output_filename, data)
