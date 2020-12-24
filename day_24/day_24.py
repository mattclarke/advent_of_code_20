from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

directions = []

for line in puzzle_input:
    temp = []
    while line:
        if line.startswith("e") or line.startswith("w"):
            temp.append(line[0])
            line = line[1:]
        else:
            temp.append(line[:2])
            line = line[2:]
    directions.append(temp)

print(directions)

flipped_tiles = {}

for direction in directions:
    position = [0, 0]
    for step in direction:
        if step == "e":
            position[0] += 2
        elif step == "w":
            position[0] -= 2
        elif step == "se":
            position[0] += 1
            position[1] -= 1
        elif step == "ne":
            position[0] += 1
            position[1] += 1
        elif step == "sw":
            position[0] -= 1
            position[1] -= 1
        elif step == "nw":
            position[0] -= 1
            position[1] += 1
        else:
            assert False
    position = (position[0], position[1])
    tile = flipped_tiles.get(position, False)
    tile = True if tile is False else False
    flipped_tiles[position] = tile

# print(len(flipped_tiles))

total = 0
for k,v in flipped_tiles.items():
    if v:
        total += 1

# 275
print(f"answer = {total}")


# Part 2
# From part one generate day 0
black_tiles = {x for x, v in flipped_tiles.items() if v}
# print(black_tiles)
#
# print(f"Day 0: {len(black_tiles)}")

neighbours = [(2,0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]


def do_tick(board):
    new_board = set()
    for x in range(-200, 200):
        for y in range(-200, 200):
            num = 0
            for n in neighbours:
                nx = x + n[0]
                ny = y + n[1]
                if (nx, ny) in board:
                    num += 1
            if (x, y) in board:
                if num in [1,2]:
                    new_board.add((x, y))
            else:
                if num == 2:
                    new_board.add((x, y))
    return new_board


for i in range(100):
    black_tiles = do_tick(black_tiles)
    # print(f"Day {i+1}: {len(black_tiles)}")

# 3537
print(f"answer = {len(black_tiles)}")
