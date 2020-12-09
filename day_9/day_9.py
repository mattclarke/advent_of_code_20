with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

PREAMBLE_LEN = 25

# PUZZLE_INPUT = """
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# """
# PREAMBLE_LEN = 5

puzzle_input = PUZZLE_INPUT.strip().split("\n")
puzzle_input = [int(x) for x in puzzle_input]

print(puzzle_input)

last_values = []
values = set()

for i in range(PREAMBLE_LEN):
    curr = puzzle_input.pop(0)
    last_values.append(curr)
    values.add(curr)

ANSWER = -1

while puzzle_input:
    current = puzzle_input.pop(0)
    found = False
    for i in last_values:
        target = current - i
        if target in values:
            found = True
            break
    if not found:
        ANSWER = current
        break
    first = last_values.pop(0)
    values.remove(first)
    last_values.append(current)
    values.add(current)

# 14360655
print(f"answer = {ANSWER}")

# Part 2
puzzle_input = PUZZLE_INPUT.strip().split("\n")
puzzle_input = [int(x) for x in puzzle_input]

start = 0
end = 0
total = 0
found = False

while start < len(puzzle_input):
    total = puzzle_input[start]
    end = start + 1
    while end < len(puzzle_input):
        total += puzzle_input[end]
        if total == ANSWER:
            found = True
            break
        elif total > ANSWER:
            # Early exit
            break
        end += 1
    if found:
        break
    start += 1

cont_range = puzzle_input[start : end + 1]

# 1962331
print(f"answer = {min(cont_range) + max(cont_range)}")
