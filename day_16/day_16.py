with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# """

# Part 2 only
# PUZZLE_INPUT = """
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

rules = []
my_ticket = None
nearby = []

position = 0

for i in puzzle_input:
    if i == "":
        position += 1
        continue
    if i.startswith("your") or i.startswith("nearby"):
        continue
    if position == 0:
        rules.append(i)
    elif position == 1:
        my_ticket = [int(x) for x in i.split(",")]
    elif position == 2:
        nearby.append(i)
    else:
        assert False

valid_numbers = set()

invalid_numbers = []

# These are for part 2
valid_tickets = []
rule_names = {}

for rule in rules:
    rule_names[rule[:rule.index(":")]] = []
    temp = rule[rule.index(":") + 2:]
    ranges = temp.split(" or ")
    is_valid = True
    for r1 in ranges:
        vals = r1.split("-")
        vals = (int(vals[0]), int(vals[1]))
        for i in range(vals[0], vals[1] + 1):
            valid_numbers.add(i)
            rule_names[rule[:rule.index(":")]].append(i)

# print(valid_numbers)

for n in nearby:
    vals = [int(x) for x in n.split(",")]
    is_valid = True
    for v in vals:
        if v not in valid_numbers:
            invalid_numbers.append(v)
            is_valid = False
            break
    if is_valid:
        valid_tickets.append(vals)
# print(invalid_numbers)

# 24110
print(f"answer = {sum(invalid_numbers)}")


# Part 2
# print(rule_names)
# print(valid_tickets)

# For positions assign all the rules
tracker = {}
for i in range(len(rule_names)):
    tracker[i] = set(rule_names.keys())

# print(tracker)

# Go through all the tickets and remove invalid rules for each position
for ticket in valid_tickets:
    for i, t in enumerate(ticket):
        for k,v in rule_names.items():
            if t not in v:
                tracker[i].remove(k)

# print(tracker)

found = set()

# Go through all the positions, if it has only one rule then we have found the
# rule for that position, so that rule can be removed for the other positions.
# Eventually all positions will only have one rule and we are done.
while True:
    finished = True
    for n, v in tracker.items():
        if len(v) == 1:
            found |= v
        else:
            finished = False
            new_v = set()
            for i in v:
                if i not in found:
                    new_v.add(i)
            tracker[n] = new_v

    if finished:
        break

# print(tracker)

answer = 1

for i, v in tracker.items():
    name = v.pop()
    if name.startswith("departure"):
        answer *= my_ticket[i]


# 6766503490793
print(f"answer = {answer}")

