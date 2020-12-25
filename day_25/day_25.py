from copy import copy

PUZZLE_INPUT = """
16616892
14505727
"""

# PUZZLE_INPUT = """
# 5764801
# 17807724
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

card_pub = int(puzzle_input[0])
door_pub = int(puzzle_input[1])

subject_number = 7

# Find card loop size
value = 1
card_loop_size = 0

while value != card_pub:
    value *= subject_number
    value = value % 20201227
    card_loop_size += 1
# print(card_loop_size)

# Find door loop size
value = 1
door_loop_size = 0

while value != door_pub:
    value *= subject_number
    value = value % 20201227
    door_loop_size += 1
# print(door_loop_size)

# Calculate the encryption key using the door pub
value_door = 1
for _ in range(card_loop_size):
    value_door *= door_pub
    value_door = value_door % 20201227
# print(value_door)

# Calculate the encryption key using the card pub
value_card = 1
for _ in range(door_loop_size):
    value_card *= card_pub
    value_card = value_card % 20201227
# print(value_card)

# Should be the same
assert value_card == value_door

# 4441893
print(f"answer = {value_card}")
