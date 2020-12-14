from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 939
# 7,13,x,x,59,x,31,19
# """

# For part 2 only
# 3417
PUZZLE_INPUT = """
1
17,x,13,19
"""

# 754018
# PUZZLE_INPUT = """
# 1
# 67,7,59,61
# """

# 779210
# PUZZLE_INPUT = """
# 1
# 67,x,7,59,61
# """

# 1261476
# PUZZLE_INPUT = """
# 1
# 67,7,x,59,61
# """

# 1202161486
# PUZZLE_INPUT = """
# 1
# 1789,37,47,1889
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
TIMESTAMP = int(puzzle_input[0])
values = []
for x in puzzle_input[1].split(","):
    if x == "x":
        values.append(x)
    else:
        values.append(int(x))
puzzle_input = values

print(puzzle_input)

next_times = []

for x in puzzle_input:
    if x != "x":
        base = TIMESTAMP // x
        next_times.append((x * (base + 1), x))
print(next_times)

next_bus = min(next_times)
waiting_time = next_bus[0] - TIMESTAMP

# 4135
print(f"answer = {waiting_time * next_bus[1]}")


# Part 2
ids = []
offsets = []

for i, v in enumerate(puzzle_input):
    if v != 'x':
        ids.append(v)
        offsets.append(i)
print(ids)
print(offsets)

# Chinese remainder theorem
# https://www.dave4math.com/mathematics/chinese-remainder-theorem/

a_values = []

for n, o in zip(ids, offsets):
    if o == 0:
        a_values.append(0)
    else:
        a_values.append(n - o)

print(a_values)

overall_mod = reduce(lambda x, y: x*y, ids)
print(overall_mod)

n_bar = [overall_mod // x for x in ids]
print(n_bar)

u_values = []

for i in range(len(ids)):
    n = n_bar[i]
    m = 1
    while (m * n) % ids[i] != 1:
        m += 1
    u_values.append(m)

print(u_values)

x = 0

for i in range(len(ids)):
    x += a_values[i] * n_bar[i] * u_values[i]

print(x)
# 640856202464541
print(f"answer = {x % overall_mod}")
