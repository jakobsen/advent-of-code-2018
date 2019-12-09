import re
from datetime import datetime
from collections import defaultdict

with open('04.in') as f:
    for line in f:
        raw_entries = f.read()

entry_regex = re.compile(r"\[(\d{4}\-\d{2}\-\d{2} \d{2}:\d{2})\] (.+)")

entries = {}
for groups in entry_regex.findall(raw_entries):
    entries[datetime.strptime(groups[0], '%Y-%m-%d %H:%M')] = groups[1]

guard_regex = re.compile(r"Guard #(\d+)")
current_guard = None
sleep_time = defaultdict(list)
for k, v in sorted(entries.items()):
    new_guard = guard_regex.search(v)
    if new_guard is not None:
        current_guard = int(new_guard.groups()[0])
    if v == 'falls asleep':
        sleep_start = k
    if v == 'wakes up':
        sleep_end = k
        for i in range(sleep_start.minute, sleep_end.minute):
            sleep_time[current_guard].append(i)

longest_sleep = 0
sleepiest_guard = None
for k, v in sleep_time.items():
    if len(v) > longest_sleep:
        longest_sleep = len(v)
        sleepiest_guard = k

most_times_asleep_at_minute = 0
for minute in sleep_time[sleepiest_guard]:
    if sleep_time[sleepiest_guard].count(minute) > most_times_asleep_at_minute:
        most_times_asleep_at_minute = sleep_time[sleepiest_guard].count(minute)
        sleepiest_minute = minute

most_times_asleep_at_same_minute = 0
most_consistent_minute = None
most_consistent_guard = None
for k, v in sleep_time.items():
    for minute in v:
        if v.count(minute) > most_times_asleep_at_same_minute:
            most_times_asleep_at_same_minute = v.count(minute)
            most_consistent_minute = minute
            most_consistent_guard = k

print(f"Part 1: {sleepiest_guard * sleepiest_minute}")
print(f"Part 2: {most_consistent_guard * most_consistent_minute}")