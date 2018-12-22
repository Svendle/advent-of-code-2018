# 1518-05-07,00:56,wake
# 1518-08-18,00:06,sleep
# 1518-11-11,00:04,2179
from collections import defaultdict

guard_times = defaultdict(lambda: [0]*60)

data = (line.strip().split(',') for line in open('input.txt'))
data = sorted(data, key=lambda x: x[:2])

curr_guard = None
sleep_start = None

# Build sleep time dict
for _, time, code in data:
    if code == 'sleep':
        sleep_start = int(time.split(':')[1])
    elif code == 'wake':
        sleep_end = int(time.split(':')[1])
        guard_times[curr_guard][sleep_start:sleep_end] = [x + 1 for x in guard_times[curr_guard][sleep_start:sleep_end]]
    else:
        curr_guard = int(code)

# Find most sleeping guard
guard, times = max(guard_times.items(), key=lambda x: sum(x[1]))
most_sleep = times.index(max(times))
print(most_sleep * guard)