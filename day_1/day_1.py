with open("input.txt") as f:
    puzzle_input = f.read()

# puzzle_input = """
# 1721
# 979
# 366
# 299
# 675
# 1456
# """

puzzle_input = {int(x) for x in puzzle_input.split()}
print(puzzle_input)

for i in puzzle_input:
    remainder = 2020 - i
    if remainder in puzzle_input:
        # Solve = 988771
        print(f"Answer = {i} * {remainder} = {i * remainder}")
        break

# Part 2
for i in puzzle_input:
    for j in puzzle_input:
        if i == j:
            continue
        for k in puzzle_input:
            if i == k or j == k:
                continue
            if i + j + k == 2020:
                # 171933104
                print(f"Answer = {i} * {j} * {k} = {i * j * k}")
