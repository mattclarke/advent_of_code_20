with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 1 + 2 * 3 + 4 * 5 + 6
# 1 + (2 * 3) + (4 * (5 + 6))
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

add = lambda a, b: a + b
multiply = lambda a, b: a * b
digits = [str(x) for x in range(10)]


def recurs(tokens, top=True):
    total = 0
    op = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in digits:
            v = int(token)
            if op is None:
                # First value
                total = v
            else:
                total = op(total, v)
        elif token == "+":
            op = add
        elif token == "*":
            op = multiply
        elif token == "(":
            val, j = recurs(tokens[i + 1:], False)
            if op is None:
                total = val
            else:
                total = op(total, val)
            i += j
        elif token == ")" and not top:
            return total, i + 1
        i += 1
    return total, None


total = 0
for line in puzzle_input:
    tokens = [x for x in line if x != " "]
    # print(tokens)
    # print(recurs(tokens))
    result, _ = recurs(tokens)
    total += result

# 4696493914530
print(f"answer = {total}")


# Part 2
def recurs(tokens, top=True):
    total = 0
    op = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in digits:
            v = int(token)
            if op is None:
                # First value
                total = v
            else:
                total = op(total, v)
        elif token == "+":
            op = add
        elif token == "*":
            op = multiply
            val, j = recurs(tokens[i + 1:], False)
            total = multiply(total, val)
            if j is None:
                i = len(tokens)
            else:
                i += j - 1
        elif token == "(":
            val, j = recurs(tokens[i + 1:], False)
            if op is None:
                total = val
            else:
                total = op(total, val)
            i += j
        elif token == ")" and not top:
            return total, i + 1
        i += 1
    return total, None


total = 0
for line in puzzle_input:
    tokens = [x for x in line if x != " "]
    # print(tokens)
    # print(recurs(tokens))
    result, _ = recurs(tokens)
    total += result

# 362880372308125
print(f"answer = {total}")
