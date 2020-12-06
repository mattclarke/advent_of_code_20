with open("input.txt") as f:
    puzzle_input = f.read()

# puzzle_input = """
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# """

puzzle_input = puzzle_input.strip().split("\n")
print(puzzle_input)


def calculate(dir_x, dir_y):
    x = 0
    y = 0
    trees_hit = 0

    while y < len(puzzle_input):
        if puzzle_input[y][x] == "#":
            # print(f"{x} {y}")
            trees_hit += 1
        x += dir_x
        y += dir_y
        x = x % len(puzzle_input[0])
        # print(f"{x} {y}")
    return trees_hit


# 176
print(f"answer = {calculate(3,1)}")


# Part 2
routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

for r in routes:
    ans = calculate(*r)
    total *= ans

# 5872458240
print(f"answer = {total}")
