with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """

# PUZZLE_INPUT = """
# 28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
puzzle_input = [int(x) for x in puzzle_input]
puzzle_input.sort()

# print(puzzle_input)

diffs = [puzzle_input[0]]

while puzzle_input:
    curr = puzzle_input.pop(0)
    if puzzle_input:
        diffs.append(puzzle_input[0] - curr)
# Add the max voltage diff from the last to the "adaptor" (always 3)
diffs.append(3)

# print(diffs)
# print(diffs.count(1))
# print(diffs.count(3))

# 2574
print(f"answer = {diffs.count(1) * diffs.count(3)}")

# Part 2
puzzle_input = PUZZLE_INPUT.strip().split("\n")
puzzle_input = [int(x) for x in puzzle_input]
puzzle_input.sort()
puzzle_input.insert(0, 0)
# puzzle_input.append(puzzle_input)

ways_to = []

for i, v in enumerate(puzzle_input):
    if i == 0:
        ways_to.append(1)
        continue
    tots = 0
    if i - 3 >= 0 and puzzle_input[i - 3] >= v - 3:
        tots += ways_to[i - 3]
    if i - 2 >= 0 and puzzle_input[i - 2] >= v - 3:
        tots += ways_to[i - 2]
    if i - 1 >= 0 and puzzle_input[i - 1] >= v - 3:
        tots += ways_to[i - 1]
    ways_to.append(tots)

# print(ways_to)

# 2644613988352
print(f"answer = {ways_to[~0]}")

