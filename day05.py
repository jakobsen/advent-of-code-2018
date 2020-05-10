with open("05.in") as f:
    puzzle = f.read().strip()


def react(polymer):
    stack = []
    for molecule in polymer:
        if stack and molecule == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(molecule)
    return len(stack)


def shorten(polymer):
    shortest = len(polymer)
    for i in range(26):
        remove = chr(ord("a") + i)
        trial_polymer = polymer.replace(remove, "")
        trial_polymer = trial_polymer.replace(remove.swapcase(), "")
        trial_length = react(trial_polymer)
        if trial_length < shortest:
            shortest = trial_length
    return shortest


print(f"Part 1: {react(puzzle)}")
print(f"Part 2: {shorten(puzzle)}")
