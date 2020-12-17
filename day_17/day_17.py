with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

PUZZLE_INPUT = """
.#.
..#
###
"""

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

board = {0: set()}


min_x = 100
min_y = 100
max_x = -100
max_y = -100


for y, row in enumerate(puzzle_input):
    for x, sq in enumerate(row):
        if sq == "#":
            board[0].add((x, y))


def print_board(board):
    min_z = min(board.keys())
    max_z = max(board.keys())
    for z in range(min_z, max_z + 1):
        print(f"\nz = {z}")
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                if (x, y) in board[z]:
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

# print(len(all_ps), all_ps)


def tick(board):
    new_board = {}
    count = 0
    min_z = min(board.keys())
    max_z = max(board.keys())
    for z in range(min_z - 1, max_z + 2):
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                neighbours = 0
                for p in perms_3d:
                    x1 = x + p[0]
                    y1 = y + p[1]
                    z1 = z + p[2]
                    if z1 in board and (x1, y1) in board[z1]:
                        neighbours += 1
                if z in board and (x, y) in board[z]:
                    # active
                    if neighbours in [2, 3]:
                        if z not in new_board:
                            new_board[z] = set()
                        new_board[z].add((x, y))
                        count += 1
                elif z in board:
                    # inactive
                    if neighbours == 3:
                        if z not in new_board:
                            new_board[z] = set()
                        new_board[z].add((x, y))
                        count += 1
                else:
                    # inactive
                    if neighbours == 3:
                        if z not in new_board:
                            new_board[z] = set()
                        new_board[z].add((x, y))
                        count += 1
    return new_board, count


def update_min_max(board):
    global min_x, max_x, min_y, max_y
    min_x = 10000000000
    min_y = 10000000000
    max_x = -10000000000
    max_y = -10000000000

    for z in board:
        min_y = min(min([x[1] for x in board[z]]), min_y)
        max_y = max(max([x[1] for x in board[z]]), max_y)
        min_x = min(min([x[0] for x in board[z]]), min_x)
        max_x = max(max([x[0] for x in board[z]]), max_x)


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

