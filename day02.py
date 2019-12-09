letters = []
with open('02.in') as f:
    for line in f:
        letters.append(line.strip())
twocount = 0
threecount = 0

# Part 1
for l in letters:
    if 2 in [l.count(d) for d in l]:
        twocount += 1
    if 3 in [l.count(d) for d in l]:
        threecount += 1
print(f"Part 1: {threecount * twocount}")

# Part 2
for x in letters:
    for y in letters:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])
            print(f"Part 2: {''.join(ans)}")
            exit(0)
