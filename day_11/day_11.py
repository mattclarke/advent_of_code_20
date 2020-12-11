from copy import deepcopy


with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

puzzle_input = []
for x in PUZZLE_INPUT.strip().split("\n"):
    line = ["_"]
    for y in x:
        line.append(y)
    line.append("_")
    puzzle_input.append(line)
border = ["_" for x in puzzle_input[0]]
puzzle_input.insert(0, border[:])
puzzle_input.append(border[:])

print(puzzle_input)


def get_neighbours(y, x, board):
    count = 0
    if board[y][x - 1] == "#":
        count += 1
    if board[y][x + 1] == "#":
        count += 1
    if board[y + 1][x] == "#":
        count += 1
    if board[y - 1][x] == "#":
        count += 1
    if board[y - 1][x - 1] == "#":
        count += 1
    if board[y - 1][x + 1] == "#":
        count += 1
    if board[y + 1][x - 1] == "#":
        count += 1
    if board[y + 1][x + 1] == "#":
        count += 1
    return count


def tick(current):
    result = deepcopy(current)
    for y in range(len(current)):
        if y == 0 or y == len(current) - 1:
            continue
        for x in range(len(current[y])):
            if x == 0 or x == len(current[y]) - 1:
                continue
            if current[y][x] == ".":
                continue
            num = get_neighbours(y, x, current)
            if current[y][x] == "L" and num == 0:
                result[y][x] = "#"
            elif current[y][x] == "#" and num >= 4:
                result[y][x] = "L"
    return result


last_round = deepcopy(puzzle_input)


def print_board(board):
    for y in board:
        line = "".join(y)
        print(line)


# print_board(last_round)

while True:
    new_board = tick(last_round)
    if new_board == last_round:
        break
    last_round = new_board
    # print_board(last_round)

total_occupied = 0
for y in last_round:
    total_occupied += y.count("#")

# 2247
print(f"answer = {total_occupied}")


# Part 2
def get_neighbours(y, x, board):
    count = 0
    yy = y
    xx = x
    # Go left
    def L(y, x):
        return y, x - 1

    def UL(y, x):
        return y - 1, x - 1

    def U(y, x):
        return y - 1, x

    def UR(y, x):
        return y - 1, x + 1

    def R(y, x):
        return y, x + 1

    def DR(y, x):
        return y + 1, x + 1

    def D(y, x):
        return y + 1, x

    def DL(y, x):
        return y + 1, x - 1

    for func in [L, UL, U, UR, R, DR, D, DL]:
        yy = y
        xx = x
        while True:
            yy, xx = func(yy, xx)
            if board[yy][xx] == "#":
                count += 1
                break
            if board[yy][xx] == "L" or board[yy][xx] == "_":
                break
    return count


def tick(current):
    from copy import deepcopy

    result = deepcopy(current)
    for y in range(len(current)):
        if y == 0 or y == len(current) - 1:
            continue
        for x in range(len(current[y])):
            if x == 0 or x == len(current[y]) - 1:
                continue
            if current[y][x] == ".":
                continue
            num = get_neighbours(y, x, current)
            if current[y][x] == "L" and num == 0:
                result[y][x] = "#"
            elif current[y][x] == "#" and num >= 5:
                result[y][x] = "L"
    return result


last_round = deepcopy(puzzle_input)
while True:
    new_board = tick(last_round)
    if new_board == last_round:
        break
    last_round = new_board
    # print_board(last_round)

total_occupied = 0
for y in last_round:
    total_occupied += y.count("#")

# 2011
print(f"answer = {total_occupied}")
