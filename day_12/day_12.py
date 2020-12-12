with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# F10
# N3
# F7
# R90
# F11
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
puzzle_input = [(x[0], int(x[1:])) for x in puzzle_input]

# print(puzzle_input)

dirs = {"E": (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}


def rot(current, clockwise, steps):
    for _ in range(steps):
        if current == "E":
            current = "S" if clockwise else "N"
        elif current == "S":
            current = "W" if clockwise else "E"
        elif current == "W":
            current = "N" if clockwise else "S"
        elif current == "N":
            current = "E" if clockwise else "W"
    return current


# x y
position = (0, 0)
direction = "E"

for cmd, val in puzzle_input:
    if cmd == "F":
        position = (
            position[0] + val * dirs[direction][0],
            position[1] + val * dirs[direction][1],
        )
    elif cmd == "N":
        position = (position[0], position[1] - val)
    elif cmd == "S":
        position = (position[0], position[1] + val)
    elif cmd == "E":
        position = (position[0] + val, position[1])
    elif cmd == "W":
        position = (position[0] - val, position[1])
    elif cmd == "R":
        steps = val // 90
        direction = rot(direction, True, steps)
    elif cmd == "L":
        steps = val // 90
        direction = rot(direction, False, steps)

distance = abs(position[0]) + abs(position[1])

# 2057
print(f"answer = {distance}")


# Part 2
wp_position = (10, -1)
position = (0, 0)


def rot(current, clockwise, steps):
    if steps == 2:
        return -current[0], -current[1]

    if steps == 3:
        steps = 1
        clockwise = not clockwise

    new_dir = abs(current[1]), abs(current[0])

    # SE
    if current[0] >= 0 and current[1] >= 0:
        # SW or NE
        return (-new_dir[0], new_dir[1]) if clockwise else (new_dir[0], -new_dir[1])
    # NE
    elif current[0] >= 0 and current[1] < 0:
        # SE or NW
        return (new_dir[0], new_dir[1]) if clockwise else (-new_dir[0], -new_dir[1])
    # NW
    elif current[0] < 0 and current[1] < 0:
        # NE or SW
        return (new_dir[0], -new_dir[1]) if clockwise else (-new_dir[0], new_dir[1])
    # SW
    elif current[0] < 0 and current[1] >= 0:
        # NW or SE
        return (-new_dir[0], -new_dir[1]) if clockwise else (new_dir[0], new_dir[1])
    else:
        assert False


for cmd, val in puzzle_input:
    if cmd == "F":
        position = (
            position[0] + val * wp_position[0],
            position[1] + val * wp_position[1],
        )
    elif cmd == "N":
        wp_position = (wp_position[0], wp_position[1] - val)
    elif cmd == "S":
        wp_position = (wp_position[0], wp_position[1] + val)
    elif cmd == "E":
        wp_position = (wp_position[0] + val, wp_position[1])
    elif cmd == "W":
        wp_position = (wp_position[0] - val, wp_position[1])
    elif cmd == "R":
        steps = val // 90
        wp_position = rot(wp_position, True, steps)
    elif cmd == "L":
        steps = val // 90
        wp_position = rot(wp_position, False, steps)

distance = abs(position[0]) + abs(position[1])

# 71504
print(f"answer = {distance}")
