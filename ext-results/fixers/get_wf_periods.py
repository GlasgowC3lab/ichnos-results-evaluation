import sys
import pandas as pd
import os, csv


class TraceRecord:
    """
    A class to parse raw task trace data into a structured format and 
    convert it into a CarbonRecord instance.
    """
    def __init__(self, fields: str, data: str, delimiter: str) -> None:
        """
        Initialize a TraceRecord.
        
        :param fields: A delimited string of field names.
        :param data: A delimited string of data corresponding to the fields.
        :param delimiter: The delimiter to split fields and data.
        """
        self._raw = self.get_raw_data_map(fields, data, delimiter)
        self._duration = self._raw['duration']
        self._start = self._raw.get('Start timestamp')
        self._complete = self._raw.get('End timestamp')
        self._task_id = self._raw['Id']
        self._hostname = self._raw['Hostname']

    def get_raw_data_map(self, fields: str, data: str, delimiter: str) -> dict:
        """
        Convert the raw data strings into a dictionary mapping field names to values.
        
        :param fields: Delimited string of field names.
        :param data: Delimited string of field values.
        :param delimiter: Delimiter used in the strings.
        :return: Dictionary of raw data.
        """
        raw = {}
        for field, value in zip(fields.split(delimiter), data.split(delimiter)):
            value = value.strip()
            if field == "Memory":
                value = None if value == '-' else float(value)
            elif field == "duration":
                value = float(value)
            raw[field] = value
        return raw 

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def start(self):
        return self._start

    @property
    def complete(self):
        return self._complete

    @property
    def task_id(self):
        return self._task_id

    @property
    def hostname(self):
        return self._hostname

    @property
    def complete(self):
        return self._complete
    @complete.setter
    def complete(self, value):  
        self._complete = value

    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, value):
        self._start = value

    def __str__(self) -> str:
        """
        Return the string representation of this TraceRecord.
        """
        return f"[TraceRecord: {str(self._raw)}]"


# Default Values
DEFAULT = "default"
DELIMITER = ","


# Functions
def parse_trace_file(filepath):
    with open(filepath, 'r') as file:
        lines = [line.rstrip() for line in file]

    header = lines[0]
    records = []

    for line in lines[1:]:
        trace_record = TraceRecord(header, line, DELIMITER)
        records.append(trace_record)

    return records



def get_timeline_data(record: TraceRecord):
    data = {}

    data["duration"] = record.duration
    data["start"] = record.start
    data["complete"] = record.complete
    data["hostname"] = record.hostname
    
    return data


def get_tasks_by_hour(start_hour, end_hour, tasks):
    tasks_by_hour = {}

    step = 60 * 60 * 1000  # 60 minutes in ms
    i = start_hour - step  # start an hour before to be safe

    while i <= end_hour:
        data = [] 

        for task in tasks: 
            # full task is within this hour
            if int(task["start"]) >= i and int(task["complete"]) <= i + step:
                data.append(task)
            # task ends within this hour (but starts in a previous hour)
            elif int(task["complete"]) > i and int(task["complete"]) <= i + step and int(task["start"]) < i:
                # add task from start of this hour until end of hour
                partial_task = task.copy()
                partial_task["start"] = i
                data.append(partial_task)
            # task starts within this hour (but ends in a later hour)
            elif int(task["start"]) > i and int(task["start"]) <= i + step and int(task["complete"]) > i + step: 
                # add task from start to end of this hour
                partial_task = task.copy()
                partial_task["complete"] = i + step
                data.append(partial_task)
            # task starts before hour and ends after this hour
            elif int(task["start"]) < i and int(task["complete"]) > i + step:
                partial_task = task.copy()
                partial_task["start"] = i
                partial_task["end"] = i + step
                data.append(partial_task)

        tasks_by_hour[i] = data
        i += step

    return tasks_by_hour


def get_tasks(filename):
    records = parse_trace_file(f"{filename}.csv")
    data_records = []

    for record in records:
        data = get_timeline_data(record)
        data_records.append(data)

    return data_records


def get_node_active_periods(tasks):
    """
    Return a dictionary mapping each node to a list of (start, end) intervals
    when at least one task was running on that node.
    Overlapping task intervals are merged into continuous periods.
    """
    tasks_by_node = {}
    for task in tasks:
        node = task["hostname"]
        tasks_by_node.setdefault(node, []).append(task)

    active_periods = {}

    for node, node_tasks in tasks_by_node.items():
        # Sort by start time
        intervals = sorted(
            [(int(t["start"]), int(t["complete"])) for t in node_tasks],
            key=lambda x: x[0],
        )

        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        active_periods[node] = [(s, e) for s, e in merged]

    return active_periods



def export_periods_to_csv(periods_by_node, filename_prefix):
    """
    Export a dictionary of node -> [(start, end), ...] to CSV files.
    One file per node, e.g., 'active_nodeA.csv' or 'idle_nodeB.csv'.
    """
    os.makedirs("period_exports", exist_ok=True)

    for node, periods in periods_by_node.items():
        node_out = node.split('-')[-1]
        csv_path = os.path.join("period_exports", f"{filename_prefix}_{node_out}.csv")
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["start_ms", "end_ms", "duration_ms", "start_time", "end_time"])
            for start, end in periods:
                writer.writerow([
                    start,
                    end,
                    end - start,
                    pd.to_datetime(start, unit="ms").strftime("%Y-%m-%d %H:%M:%S"),
                    pd.to_datetime(end, unit="ms").strftime("%Y-%m-%d %H:%M:%S")
                ])
        print(f"Exported {len(periods)} periods for {node} → {csv_path}")


# Main Script
if __name__ == '__main__':
    arguments = sys.argv[1:]
    filename = arguments[0]
    tasks = get_tasks(filename)
    active_times = get_node_active_periods(tasks)
    export_periods_to_csv(active_times, "active")
