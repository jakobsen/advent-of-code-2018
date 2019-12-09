from itertools import cycle

with open('01.in') as f:
    n = []
    for line in f:
        n.append(int(line))

print(f"Part 1: {sum(n)}")

seen = set()
frequency = 0
seen.add(0)
n = cycle(n)
while True:
    frequency += next(n)
    if frequency in seen:
        print(f"Part 2: {frequency}")
        break
    seen.add(frequency)