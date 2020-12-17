with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# .#.
# ..#
# ###
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

board = set()


min_x = 100
min_y = 100
min_z = 100
max_x = -100
max_y = -100
max_z = -100


for y, row in enumerate(puzzle_input):
    for x, sq in enumerate(row):
        if sq == "#":
            board.add((x, y, 0))


def print_board(board):
    for z in range(min_z, max_z + 1):
        print(f"\nz = {z}")
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                if (x, y, z) in board:
                    line.append("#")
                else:
                    line.append(".")

            print("".join(line))


from itertools import permutations

perms_3d = set()
perms_3d |= set(permutations([1, 0, 0]))
perms_3d |= set(permutations([1, 1, 0]))
perms_3d |= set(permutations([1, 1, 1]))
perms_3d |= set(permutations([-1, 0, 0]))
perms_3d |= set(permutations([-1, -1, 0]))
perms_3d |= set(permutations([-1, -1, -1]))
perms_3d |= set(permutations([-1, -1, 1]))
perms_3d |= set(permutations([-1, 1, 1]))
perms_3d |= set(permutations([1, -1, 0]))

# Should be 26
assert len(perms_3d) == 26

# print(len(all_ps), all_ps)


def tick(board):
    new_board = set()
    count = 0
    for z in range(min_z - 1, max_z + 2):
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                neighbours = 0
                for p in perms_3d:
                    x1 = x + p[0]
                    y1 = y + p[1]
                    z1 = z + p[2]
                    if (x1, y1, z1) in board:
                        neighbours += 1
                if (x, y, z) in board:
                    # active
                    if neighbours in [2, 3]:
                        new_board.add((x, y, z))
                        count += 1
                else:
                    # inactive
                    if neighbours == 3:
                        new_board.add((x, y, z))
                        count += 1
    return new_board, count


def update_min_max(board):
    global min_x, max_x, min_y, max_y, min_z, max_z
    min_x = 10000000000
    min_y = 10000000000
    min_z = 10000000000
    max_x = -10000000000
    max_y = -10000000000
    max_z = -10000000000

    for x, y, z in board:
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)


update_min_max(board)
print_board(board)

count = 0

for i in range(6):
    board, count = tick(board)
    update_min_max(board)
    # print(f"______ {i + 1} ________")
    # print_board(board)
    # print(count)

# 306
print(f"answer = {count}")


# Day 2
perms_4d = set()
perms_4d |= set(permutations([1, 0, 0, 0]))
perms_4d |= set(permutations([-1, 0, 0, 0]))
perms_4d |= set(permutations([1, 1, 0, 0]))
perms_4d |= set(permutations([-1, 1, 0, 0]))
perms_4d |= set(permutations([-1, -1, 0, 0]))
perms_4d |= set(permutations([1, 1, 1, 0]))
perms_4d |= set(permutations([-1, 1, 1, 0]))
perms_4d |= set(permutations([-1, -1, 1, 0]))
perms_4d |= set(permutations([-1, -1, -1, 0]))
perms_4d |= set(permutations([1, 1, 1, 1]))
perms_4d |= set(permutations([-1, 1, 1, 1]))
perms_4d |= set(permutations([-1, -1, 1, 1]))
perms_4d |= set(permutations([-1, -1, -1, 1]))
perms_4d |= set(permutations([-1, -1, -1, -1]))

# Should be 80
assert len(perms_4d) == 80

board = set()

min_x = 100
min_y = 100
min_z = 100
min_w = 100
max_x = -100
max_y = -100
max_z = -100
max_w = -100


def update_min_max(board):
    global min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w
    min_x = 10000000000
    min_y = 10000000000
    min_z = 10000000000
    min_w = 10000000000
    max_x = -10000000000
    max_y = -10000000000
    max_z = -10000000000
    max_w = -10000000000

    for x, y, z, w in board:
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        min_w = min(w, min_w)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)
        max_w = max(w, max_w)


for y, row in enumerate(puzzle_input):
    for x, sq in enumerate(row):
        if sq == "#":
            board.add((x, y, 0, 0))


def tick(board):
    global min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w
    new_board = set()
    count = 0
    for w in range(min_w - 1, max_w + 2):
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    neighbours = 0
                    for p in perms_4d:
                        x1 = x + p[0]
                        y1 = y + p[1]
                        z1 = z + p[2]
                        w1 = w + p[3]
                        if (x1, y1, z1, w1) in board:
                            neighbours += 1
                    add_it = False
                    if (x, y, z, w) in board:
                        # active
                        if neighbours in [2, 3]:
                            add_it = True
                    else:
                        # inactive
                        if neighbours == 3:
                            add_it = True
                    if add_it:
                        new_board.add((x, y, z, w))
                        count += 1
    update_min_max(new_board)
    return new_board, count


update_min_max(board)

count = 0

for i in range(6):
    board, count = tick(board)

# 2572
print(f"answer = {count}")
