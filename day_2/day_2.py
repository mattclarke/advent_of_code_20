with open("input.txt") as f:
    puzzle_input = f.read()

# puzzle_input = """
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """

lines = puzzle_input.strip().split("\n")

total_valid = 0

for i, l in enumerate(lines):
    lower = int(l[0 : l.index("-")])
    higher = int(l[l.index("-") + 1 : l.index(" ")])
    char = l[l.index(" ") : l.index(":")].strip()
    password = l[l.index(":") + 1 :].strip()
    print(f"{lower} {higher} {char} {password}")
    count = password.count(char)
    if lower <= count <= higher:
        total_valid += 1

# 586
print(f"answer = {total_valid}")

# Part 2
total_valid = 0

for i, l in enumerate(lines):
    lower = int(l[0 : l.index("-")])
    higher = int(l[l.index("-") + 1 : l.index(" ")])
    char = l[l.index(" ") : l.index(":")].strip()
    password = l[l.index(":") + 1 :].strip()
    print(f"{lower} {higher} {char} {password}")
    if password[lower - 1] == char or password[higher - 1] == char:
        if password[lower - 1] != password[higher - 1]:
            total_valid += 1

# 352
print(f"answer = {total_valid}")
