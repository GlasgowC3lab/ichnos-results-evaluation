import sys
from datetime import datetime, date, timezone, timedelta


def main(args):
    filename = args[1]

    try:
        start_date = datetime.strptime(args[2], "%Y-%m-%d").date()
    except ValueError:
        print("Error: start_date must be in YYYY-MM-DD format (e.g., 2025-10-22).")
        sys.exit(1)

    utc_offset = int(args[3]) if len(args) > 3 else 2
    tz = timezone(timedelta(hours=utc_offset))

    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)

    pref = '/'.join(filename.split('/')[:-1])
    actual = filename.split('/')[-1]
    output_file = pref + "/conv-" + actual
    current_date = start_date
    previous_time = None

    with open(output_file, "w") as out:
        for i, line in enumerate(lines):
            # if it's an energy line
            if i % 2 == 0:
                out.write(line + "\n")
                continue

            # if it's a timestamp line
            try:
                t = datetime.strptime(line, "%H:%M:%S.%f").time()
            except ValueError:
                print(f"Skipping invalid timestamp: {line}")
                continue

            if previous_time and t < previous_time:
                current_date += timedelta(days=1)

            dt = datetime.combine(current_date, t).replace(tzinfo=tz)
            epoch_ms = int(dt.timestamp() * 1000)
            out.write(f"{epoch_ms}\n")

            previous_time = t

"""
Convert timestamps of format HH:MM:SS.mmm (local time) into epoch milliseconds.

Usage:
    python convert_timestamps.py <filename> <start_date> [utc_offset]

Example:
    python convert_timestamps.py timestamps.txt 2025-10-22 2
"""
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_timestamps.py <filename> <start_date> [utc_offset]")
        sys.exit(1)

    main(sys.argv)
