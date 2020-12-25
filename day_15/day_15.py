PUZZLE_INPUT = "9,3,1,0,8,4"

# PUZZLE_INPUT = "3,1,2"

puzzle_input = [int(x) for x in PUZZLE_INPUT.split(",")]
print(puzzle_input)

turn = 0
record = {}
last = 0

for i in puzzle_input:
    turn += 1
    record[i] = [turn]
    last = i

while turn < 2020:
    turn += 1
    if len(record[last]) == 1:
        last = 0
    else:
        last = record[last][1] - record[last][0]
    if last not in record:
        record[last] = []
    if len(record[last]) == 2:
        record[last][0] = record[last][1]
        record[last][1] = turn
    else:
        record[last].append(turn)
    # print(turn, ":", last)

# 371
print(f"answer = {last}")

tracker = []

# Part 2
while turn < 30_000_000:
    turn += 1
    if len(record[last]) == 1:
        last = 0
    else:
        last = record[last][1] - record[last][0]
    if last not in record:
        record[last] = []
    if len(record[last]) == 2:
        record[last][0] = record[last][1]
        record[last][1] = turn
    else:
        record[last].append(turn)
    # if last == 0:
    #     print(turn, len(tracker), tracker)
    #     tracker.clear()
    # tracker.append(last)
    # print(turn, ":", last)

# 352
print(f"answer = {last}")
