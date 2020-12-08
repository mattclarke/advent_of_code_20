with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

instructions = []

for line in puzzle_input:
    front, back = line.split(" ")
    instructions.append((front, int(back)))


def nop(value, ptr, acc):
    return ptr + 1, acc


def jmp(value, ptr, acc):
    return ptr + value, acc


def acc(value, ptr, acc):
    return ptr + 1, acc + value


commands = {
    "nop": nop,
    "jmp": jmp,
    "acc": acc,
}

accumulator = 0
pointer = 0
visited = set()

while True:
    if pointer in visited:
        break
    visited.add(pointer)
    cmd, value = instructions[pointer]
    # print(cmd, value, pointer, accumulator)
    pointer, accumulator = commands[cmd](value, pointer, accumulator)

# 1337
print(f"answer = {accumulator}")

# Part 2
for i, v in enumerate(instructions):
    new_instructions = instructions[:]
    if v[0] == "nop":
        new_instructions[i] = ("jmp", v[1])
    elif v[0] == "jmp":
        new_instructions[i] = ("nop", v[1])
    else:
        continue

    accumulator = 0
    pointer = 0
    visited = set()
    while pointer < len(new_instructions):
        if pointer in visited:
            # It is an infinite loop
            break
        visited.add(pointer)
        cmd, value = new_instructions[pointer]
        # print(cmd, value, pointer, accumulator)
        pointer, accumulator = commands[cmd](value, pointer, accumulator)
    if pointer >= len(new_instructions):
        print(f"answer = {accumulator}")
        break


