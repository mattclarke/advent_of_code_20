with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

group_answer_count = []
yes_answers = set()

for line in puzzle_input:
    if line == "":
        group_answer_count.append(len(yes_answers))
        yes_answers.clear()
        continue
    for c in line:
        yes_answers.add(c)
group_answer_count.append(len(yes_answers))

# 6161
print(f"answer = {sum(group_answer_count)}")

# Part 2
group_answer_count = []
yes_answers = {}
count = 0

for line in puzzle_input:
    if line == "":
        total = 0
        for k, v in yes_answers.items():
            if v == count:
                total += 1
        group_answer_count.append(total)
        yes_answers.clear()
        count = 0
        continue
    count += 1
    for c in line:
        yes_answers[c] = yes_answers.get(c, 0) + 1

total = 0
for k, v in yes_answers.items():
    if v == count:
        total += 1
group_answer_count.append(total)

# 2971
# print(group_answer_count)
print(f"answer = {sum(group_answer_count)}")

# Using sets
group_answer_count = []
yes_answers = set()
is_new = True

for line in puzzle_input:
    if line == "":
        group_answer_count.append(len(yes_answers))
        yes_answers.clear()
        is_new = True
        continue
    answers = set()
    last_line = line
    for c in line:
        answers.add(c)
    if is_new:
        yes_answers = answers
        is_new = False
    else:
        yes_answers &= answers
group_answer_count.append(len(yes_answers))

print(f"answer = {sum(group_answer_count)}")
