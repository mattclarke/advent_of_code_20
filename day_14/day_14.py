with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

memory = {}
mask = ""


def apply_mask(mask, value):
    result = []
    for m, v in zip(mask, value):
        if m == "X":
            result.append(v)
        else:
            result.append(m)
    return "".join(result)


for cmd in puzzle_input:
    if cmd.startswith("mask"):
        mask = cmd.replace("mask = ", "")
    else:
        address = int(cmd[cmd.index("[") + 1 : cmd.index("]")])
        value = int(cmd[cmd.index("=") + 2 :])
        value = "{0:b}".format(value).zfill(36)
        masked = apply_mask(mask, value)
        memory[address] = int(masked, 2)

total = 0
for n, v in memory.items():
    total += v

# 5902420735773
print(f"answer = {total}")


# Part 2
# PUZZLE_INPUT = """
# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# """

# Second attempt - first attempt used itertools' permutation and had too many
# repetitions
def apply_mask(mask, value):
    result = []
    for m, v in zip(mask, value):
        if m == "X":
            result.append("X")
        else:
            val = m if m == "1" else v
            result.append(val)
    return "".join(result)


def get_perms(n):
    input = [0] * n
    results = []

    def _recu(val, n):
        if n == len(val):
            return
        _recu(val[:], n+1)
        val[n] = 1
        results.append(val)
        _recu(val[:], n + 1)

    results.append(input[:])
    _recu(input[:], 0)
    return results


# Eliminate some binary conversions and generate permutations manually
def get_addresses(mask, address):
    results = set()
    masked = apply_mask(mask, address)
    indexes = [i for i, x in enumerate(masked) if x == "X"]

    # Add the initial
    copied = masked.replace("X", "0")
    initial_value = int(copied, 2)
    results.add(initial_value)

    perms = get_perms(len(indexes))

    for perm in perms:
        value = initial_value
        for i, p in enumerate(perm):
            if p == 1:
                value = value + 2 ** (35 - indexes[i])
                # if value in results:
                #     print("Repeat")
                results.add(value)
    return results


puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

memory = {}
mask = ""

for i, cmd in enumerate(puzzle_input):
    if cmd.startswith("mask"):
        mask = cmd.replace("mask = ", "")
    else:
        address = int(cmd[cmd.index("[") + 1 : cmd.index("]")])
        address = "{0:b}".format(address).zfill(36)
        value = int(cmd[cmd.index("=") + 2:])
        for add in get_addresses(mask, address):
            memory[add] = value

total = 0
for n, v in memory.items():
    total += v

# 3801988250775
print(f"answer = {total}")
