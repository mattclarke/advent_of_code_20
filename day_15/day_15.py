PUZZLE_INPUT = "9,3,1,0,8,4"

# PUZZLE_INPUT = "0,3,6"

puzzle_input = [int(x) for x in PUZZLE_INPUT.split(",")]
print(puzzle_input)

turn = 0
record = {}
last = 0

for i in puzzle_input:
    if turn == 0:
        turn += 1
        last = i
        continue
    # Put the previous value in to record
    record[last] = turn
    turn += 1
    last = i

while turn < 2020:
    prev = record.get(last, -1)
    # Put the previous value into the record
    record[last] = turn

    if prev == -1:
        # New value
        last = 0
    else:
        last = turn - prev
    turn += 1
    # print(last)



# 371
print(f"answer = {last}")

tracker = []

# Part 2
while turn < 30_000_000:
    prev = record.get(last, -1)
    record[last] = turn

    if prev == -1:
        last = 0
    else:
        last = turn - prev
    turn += 1
    # print(last)

# 352
print(f"answer = {last}")
