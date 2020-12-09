with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """
#
# PUZZLE_INPUT = """
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

bag_heir = {}

for line in puzzle_input:
    # Break up the strings
    line = line.replace(" bags", "").replace(" bag", "").replace(".", "")
    top_bag, rest = line.split(" contain ")
    contents = rest.split(", ")
    # print(f"{top_bag} {contents}")
    bag_heir[top_bag] = {}
    for c in contents:
        if c == "no other":
            continue
        num = c[0 : c.index(" ")]
        bag = c[c.index(" ") + 1 :]
        bag_heir[top_bag][bag] = num
    # print(f"{top_bag} {bag_heir[top_bag]}")

# Find the bags that can hold shiny gold directly
holders = set()
hold_queue = []

for n, v in bag_heir.items():
    if "shiny gold" in v:
        hold_queue.append(n)

while hold_queue:
    bag = hold_queue.pop(0)
    holders.add(bag)
    for n, v in bag_heir.items():
        if bag in v:
            hold_queue.append(n)

# 169
print(f"answer = {len(holders)}")

# Part 2
hold_queue = ["shiny gold"]
bag_count = -1

while hold_queue:
    bag = hold_queue.pop(0)
    bag_count += 1
    for n, v in bag_heir[bag].items():
        for i in range(int(v)):
            hold_queue.append(n)

# 82372
print(f"answer = {bag_count}")
