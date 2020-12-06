with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# FBFBBFFRLR
# BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

highest_id = 0
occupied_seats = []  # for part 2

for boarding_pass in puzzle_input:
    rows = [x for x in range(128)]
    columns = [x for x in range(8)]
    for c in boarding_pass:
        if c in ["B", "F"]:
            if c == "F":
                rows = rows[0 : len(rows) // 2]
            else:
                rows = rows[len(rows) // 2 :]
        else:
            if c == "L":
                columns = columns[0 : len(columns) // 2]
            else:
                columns = columns[len(columns) // 2 :]
    seat_id = rows[0] * 8 + columns[0]
    # print(f"{seat_id}")
    highest_id = max(seat_id, highest_id)
    occupied_seats.append(seat_id)

# 955
print(f"answer = {highest_id}")

# Part 2
occupied_seats.sort()

missing = []
for i in range(occupied_seats[0], occupied_seats[~0]):
    if i not in occupied_seats:
        missing.append(i)

# 569
print(f"answer = {missing[0]}")
