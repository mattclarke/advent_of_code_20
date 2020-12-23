from copy import copy

PUZZLE_INPUT = "538914762"

PUZZLE_INPUT = "389125467"

puzzle_input = [int(x) for x in PUZZLE_INPUT]
print(puzzle_input)

current_cup = 0
cups = puzzle_input[:]

for i in range(100):
    print(f"\n-- move {i + 1} --")
    print(f"cups: {cups}")

    pick_up = []
    for _ in range(3):
        if current_cup + 1 < len(cups):
            pick_up.append(cups.pop(current_cup + 1))
        else:
            pick_up.append(cups.pop(0))
            current_cup -= 1

    destination = cups[current_cup] - 1
    while destination not in cups:
        destination -= 1
        if destination < 1:
            destination = max(cups)


    print(f"current cup: {cups[current_cup]}")
    print(f"pick up: {pick_up}")
    print(f"destination: {destination}")

    # Insert
    index = (cups.index(destination) + 1) % len(cups)
    if index == 0:
        for pu in pick_up:
            cups.append(pu)
    else:
        for pu in reversed(pick_up):
            cups.insert(index, pu)
            if index <= current_cup:
                current_cup += 1
    current_cup = (current_cup + 1) % len(cups)

print(f"{cups}")

index_ = cups.index(1) + 1
result = []

while cups[index_] != 1:
    result.append(str(cups[index_]))
    index_ = (index_ + 1) % len(cups)

print(f"answer = {''.join(result)}")


# Part 2
# current_cup = 0
# cups = puzzle_input[:]
# highest_cup = max(cups) + 1
#
# while len(cups) < 1_000_000:
#     cups.append(highest_cup)
#     highest_cup += 1
#
#
# for i in range(10_000_000):
#     if i % 100 == 0:
#         print(f"\n-- move {i + 1} --")
#     # print(f"cups: {cups}")
#
#     pick_up = []
#     for _ in range(3):
#         if current_cup + 1 < len(cups):
#             pick_up.append(cups.pop(current_cup + 1))
#         else:
#             pick_up.append(cups.pop(0))
#             current_cup -= 1
#
#     destination = cups[current_cup] - 1
#     while destination not in cups:
#         destination -= 1
#         if destination < 1:
#             destination = max(cups)
#
#
#     # print(f"current cup: {cups[current_cup]}")
#     # print(f"pick up: {pick_up}")
#     # print(f"destination: {destination}")
#
#     # Insert
#     index = (cups.index(destination) + 1) % len(cups)
#     if index == 0:
#         for pu in pick_up:
#             cups.append(pu)
#     else:
#         for pu in reversed(pick_up):
#             cups.insert(index, pu)
#             if index <= current_cup:
#                 current_cup += 1
#     current_cup = (current_cup + 1) % len(cups)
#
# # print(f"{cups}")
#
# index_ = (cups.index(1) + 1) % len(cups)
# result = cups[index_] * cups[(index_ + 1) % len(cups)]
#
# print(f"answer = {result}")
