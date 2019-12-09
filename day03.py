from collections import defaultdict
import numpy as np
import re

with open('03.in') as f:
    data = f.read()

fabric_regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
claims = []
for groups in fabric_regex.findall(data):
    # claims = [inches from left, inches from top, inches wide, inches tall]
    claims.append(list(map(int, groups)))

claimed_squares = defaultdict(list)
unopposed = set(range(1, len(claims)+1))
for claim in claims:
    claimID, left, top, wide, tall = claim
    for i in range(left, left+wide):
        for j in range(top, top+tall):
            claimed_squares[i, j].append(claimID)
            if len(claimed_squares[i, j]) > 1:
                for ID in claimed_squares[i, j]:
                    unopposed.discard(ID)

part1 = 0
for square in claimed_squares.values():
    if len(square) > 1:
        part1 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {unopposed.pop()}")
