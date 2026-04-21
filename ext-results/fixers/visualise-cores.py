import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
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
        self._id = self._raw['task_id']
        self._realtime = self._raw['realtime']
        self._start = self._raw.get('start')
        self._complete = self._raw.get('complete')
        self._cpu_count = self._raw['cpus']
        self._cpu_usage = self._raw['%cpu']
        self._cpu_model = self._raw.get('cpu_model')
        self._memory = self._raw['memory']
        self._name = self._raw['name']
        self._task_id = self._raw['task_id']
        self._hash = self._raw.get('hash')
        self._process = self._raw['process']
        self._realtime = self._raw['realtime']
        self._submit = self._raw['submit']
        self._hostname = self._raw['hostname']

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
            if field == "memory":
                value = None if value == '-' else float(value)
            elif field == "duration" or field == "realtime":
                value = float(value)
            elif field == "%cpu":  # format x.y%
                value = 0.0 if value[:-1] == '' else float(value[:-1])
            elif field == "cpus":
                value = 1 if value == '-' else int(value)
            elif field == "rss":
                value = None if value == '-' else float(value)
            raw[field] = value
        # where memory is not set, use rss
        if raw['memory'] is None and 'rss' in raw:
            raw['memory'] = raw['rss']
        return raw 

    @property
    def realtime(self) -> float:
        return self._realtime

    @property
    def duration(self) -> float:
        return self._realtime

    @property
    def start(self):
        return self._start

    @property
    def complete(self):
        return self._complete

    @property
    def cpu_percentage(self) -> float:
        return self._cpu_usage

    @property
    def memory(self):
        return self._memory

    @property
    def cpu_count(self) -> int:
        return self._cpu_count

    @property
    def cpu_model(self):
        return self._cpu_model

    @property
    def task_id(self):
        return self._task_id

    @property
    def hash_value(self):
        return self._hash

    @property
    def process(self):
        return self._process

    @property
    def hostname(self):
        return self._hostname

    @property
    def realtime(self):
        return self._realtime
    @realtime.setter
    def realtime(self, value: float):
        self._realtime = value

    @property
    def submit(self):
        return self._submit

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
MEMORY_COEFFICIENT = 0.392  # CCF Average (See Website)


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

    data["process"] = record.process
    data["realtime"] = record.realtime
    data["start"] = record.start
    data["complete"] = record.complete
    data["cpu_count"] = record.cpu_count
    data["cpu_usage"] = record.cpu_percentage
    data["cpu_model"] = record.cpu_model
    data["memory"] = record.memory
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


def plot_task_timeline(tasks):
    tasks_by_node = {}
    for task in tasks:
        node = task["hostname"]
        tasks_by_node.setdefault(node, []).append(task)

    for node_tasks in tasks_by_node.values():
        node_tasks.sort(key=lambda t: t["start"])

    all_starts = [int(task["start"]) for task in tasks]
    all_ends = [int(task["complete"]) for task in tasks]
    earliest = min(all_starts)
    latest = max(all_ends)
    diff = 60 * 60 * 1000  # 1 hour
    start_tick = (earliest // diff) * diff
    end_tick = (latest // diff + 1) * diff

    ticks = []
    ticklabels = []
    for t in range(start_tick, end_tick + diff, diff):
        ticks.append(t)
        ticklabels.append(pd.to_datetime(t, unit="ms").strftime("%H:%M"))
    
    fig, ax = plt.subplots(figsize=(12, 8))
    current_y = 0
    node_y_positions = {}

    for node in sorted(tasks_by_node.keys()):
        node_tasks = tasks_by_node[node]
        rows = []  
        for task in node_tasks:
            start = int(task["start"])
            placed = False
            for idx, end_time in enumerate(rows):
                if start >= end_time:
                    rows[idx] = int(task["complete"])
                    task["_y"] = current_y + idx
                    placed = True
                    break
            if not placed:
                rows.append(int(task["complete"]))
                task["_y"] = current_y + len(rows) - 1
        
        node_y_positions[node] = current_y + (len(rows) - 1) / 2
        current_y += len(rows) + 2 

    for task in tasks:
        start = int(task["start"])
        width = int(task["complete"]) - start
        if width <= 0: continue

        ax.barh(task["_y"], width, left=start, alpha=0.7, edgecolor='black')
        core_val = task["cpu_count"]
        ax.text(
            start + (width / 2), 
            task["_y"], 
            core_val, 
            va='center', 
            ha='center', 
            color='white', 
            fontweight='bold',
            fontsize=8
        )

    ax.invert_yaxis()
    ax.set_yticks([node_y_positions[n] for n in sorted(tasks_by_node.keys())])
    ax.set_yticklabels(list(sorted(tasks_by_node.keys())))
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticklabels)
    plt.xticks(rotation=45) 
    print(f"workflow {round((latest - earliest) / 1000 / 60)} minutes")
    plt.tight_layout()
    plt.show()
    return


def get_tasks(filename):
    records = parse_trace_file(f"{filename}.csv")
    data_records = []

    for record in records:
        data = get_timeline_data(record)
        data_records.append(data)

    return data_records


# Main Script
if __name__ == '__main__':
    arguments = sys.argv[1:]
    filename = arguments[0]
    tasks = get_tasks(filename)
    plot_task_timeline(tasks)
