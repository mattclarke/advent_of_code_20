from copy import deepcopy
import numpy as np


with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
# """


puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

tiles = {}
tile_num = 0
tile = []

# y is first and goes downwards
for line in puzzle_input:
    if line.startswith("Tile"):
        tile_num = int(line.replace("Tile ", "").replace(":", ""))
    elif line == "":
        from copy import deepcopy
        import numpy as np

        tiles[tile_num] = np.array(tile)
        tile = []
    else:
        row = []
        for x in line:
            if x == ".":
                row.append(0)
            else:
                row.append(1)
        tile.append(row)
tiles[tile_num] = np.array(tile)

# print(tiles)

from math import sqrt

SIDE_LENGTH = int(sqrt(len(tiles)))
# print(SIDE_LENGTH)

transformations = ["", "r", "l", "rr", "f", "fr", "fl", "frr"]


def do_transform(tile, transform):
    new_tile = deepcopy(tile)
    for t in transform:
        if t == "r":
            new_tile = np.rot90(new_tile, 3)
        elif t == "l":
            new_tile = np.rot90(new_tile)
        elif t == "f":
            new_tile = np.flipud(new_tile)
        else:
            assert False
    return new_tile


result = [[None for _ in range(SIDE_LENGTH)] for _ in range(SIDE_LENGTH)]

list_of_tiles = list(tiles.keys())

# Hold the transformations
trans_cache = {}

for tile_name in list_of_tiles:
    trans = []
    for t in transformations:
        tile = do_transform(tiles[tile_name], t)
        trans.append(tile)
    trans_cache[tile_name] = trans


# Check to see which tiles can go with which
allowed_neighbours = {}

for tile_1 in list_of_tiles:
    allowed_neighbours[tile_1] = set()

    for tile_2 in list_of_tiles:
        if tile_1 == tile_2:
            continue
        for t1 in trans_cache[tile_1]:
            for t2 in trans_cache[tile_2]:
                if False not in np.equal(t1[:, ~0], t2[:, 0]):
                    allowed_neighbours[tile_1].add(tile_2)


def solve(possible_tiles, y, x):
    # print(possible_tiles, y, x)
    for tile_name in possible_tiles:

        # Skip tiles that don't appear in allowed neighbours
        if y == 0 and x == 0:
            pass
        elif y == 0:
            # Compare left only
            left = result[y][x - 1][0]
            if tile_name not in allowed_neighbours[left]:
                continue
        elif x == 0:
            # Compare up only
            up = result[y - 1][x][0]
            if tile_name not in allowed_neighbours[up]:
                continue
        else:
            # Compare up and left
            up = result[y - 1][x][0]
            if tile_name not in allowed_neighbours[up]:
                continue
            left = result[y][x - 1][0]
            if tile_name not in allowed_neighbours[left]:
                continue

        new_list = deepcopy(possible_tiles)
        new_list.remove(tile_name)

        # Tile matches neighbour(s), so just need to try the different orientations
        for tile in trans_cache[tile_name]:
            # put in if fits
            if y == 0 and x == 0:
                result[y][x] = (tile_name, tile)
            elif y == 0:
                # Compare to the left only
                left = result[y][x - 1][1]
                if False in np.equal(left[:, ~0], tile[:, 0]):
                    continue
                result[y][x] = (tile_name, tile)
            elif x == 0:
                # Compare up only
                up = result[y - 1][x][1]
                if False in np.equal(up[~0, :], tile[0, :]):
                    continue
                result[y][x] = (tile_name, tile)
            else:
                # Compare up and left
                up = result[y - 1][x][1]
                if False in np.equal(up[~0, :], tile[0, :]):
                    continue
                left = result[y][x - 1][1]
                if False in np.equal(left[:, ~0], tile[:, 0]):
                    continue
                result[y][x] = (tile_name, tile)
            # for remaining tiles see if one fits in next space
            new_x = x
            new_y = y
            if x < SIDE_LENGTH - 1:
                new_x += 1
            elif y < SIDE_LENGTH - 1:
                new_x = 0
                new_y += 1
            else:
                # No more squares, so finished
                return True
            if solve(new_list, new_y, new_x):
                return True
            result[y][x] = None


solve(list_of_tiles, 0, 0)

total = 1
total *= result[0][0][0]
total *= result[0][~0][0]
total *= result[~0][0][0]
total *= result[~0][~0][0]

# 17148689442341
print(f"answer = {total}")


# Part 2
# Construct one image
image = []

for col in result:
    i = 0
    while i < len(col[0][1]) - 1:
        if i == 0:
            i += 1
            continue
        new_col = []
        for part in col:
            new_col.extend(part[1][i][1:-1])
        image.append(new_col)
        i += 1

image = np.array(image)

print(image)

monster_raw = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

lines = monster_raw.split("\n")

squares_per_monster = 0
monster = []

for l in lines:
    if l == "":
        continue
    data = []
    for c in l:
        if c == "#":
            data.append(1)
            squares_per_monster += 1
        else:
            data.append(0)
    monster.append(data)
# print(monster)

# Use left most point as the origin of the monster
origin_r = 1
origin_c = 0
len_monster = len(monster[origin_r])


found_monsters = 0

for t in transformations:
    test_image = do_transform(image, t)

    for i, row in enumerate(test_image):
        if i == 0 or i == len(test_image) - 1:
            continue
        for j, col in enumerate(row):
            if j == 0:
                continue

            if j + len_monster > len(row):
                break
            found = True
            for k, m in enumerate(monster[origin_r]):
                if m == 1 and row[j + k] != 1:
                    found = False
                    break
            if found:
                # try top
                top_row = test_image[i - 1][j:]
                for k, m in enumerate(monster[origin_r - 1]):
                    if m == 1 and top_row[k] != 1:
                        found = False
                        break
                if found:
                    bottom_row = test_image[i + 1][j:]
                    for k, m in enumerate(monster[origin_r + 1]):
                        if m == 1 and bottom_row[k] != 1:
                            found = False
                            break
                if found:
                    found_monsters += 1

    if found_monsters > 0:
        break

print(f"monsters = {found_monsters}")
total = sum(sum(image)) - (squares_per_monster * found_monsters)

# 2009
print(f"answer = {total}")
