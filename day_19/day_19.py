with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb
# """

# Part 2
# PUZZLE_INPUT = """
# 42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1
#
# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

rules_raw = []
messages = []

in_messages = False
for line in puzzle_input:
    if in_messages:
        messages.append(line)
    elif line == "":
        in_messages = True
    else:
        rules_raw.append(line)

rules = {}

values = {}

for r in rules_raw:
    n = r[: r.index(":")]
    r = r[r.index(":") + 1 :].strip()
    if r.startswith('"'):
        values[n] = r.strip().replace('"', "")
# print(values)

for r in rules_raw:
    n = r[: r.index(":")]
    r = r[r.index(":") + 1 :].strip()
    # print(r)
    if r.startswith('"'):
        rules[n] = r.strip().replace('"', "")
    elif "|" in r:
        rs = r.split(" | ")
        r1 = []
        r2 = []
        for v in rs[0].split(" "):
            r1.append(v)
        for v in rs[1].split(" "):
            r2.append(v)
        rules[n] = (r1, r2)
    else:
        r1 = []
        for v in r.split(" "):
            r1.append(v)
        rules[n] = (r1,)
# print(rules)


def get_combos():
    def recu(node, so_far):
        values = rules[node]
        if isinstance(values, tuple):
            stems = []
            for v in values:
                temp = so_far[:]
                for n in v:
                    temp = recu(n, temp)
                stems.extend(temp)
            return stems
        else:
            if so_far:
                new_so_far = []
                for f in so_far:
                    new_so_far.append(f + values)
                return new_so_far
            else:
                return [values]

    return recu("0", [])


combos = set(get_combos())
# print(combos)

total = 0
for m in messages:
    if m in combos:
        total += 1

# 160
print(f"answer = {total}")


# Part 2

rules["8"] = (["42"], ["42", "8"])
rules["11"] = (["42", "31"], ["42", "11", "31"])


def get_combos(n):
    def recu(node, so_far):
        values = rules[node]
        if isinstance(values, tuple):
            stems = []
            for v in values:
                temp = so_far[:]
                for n in v:
                    if n == "8" or n == "11":
                        if n == "11":
                            n = "E"
                        if temp:
                            temp = [x + n for x in temp]
                        else:
                            temp = [n]
                    else:
                        temp = recu(n, temp)
                stems.extend(temp)
            return stems
        else:
            if so_far:
                new_so_far = []
                for f in so_far:
                    new_so_far.append(f + values)
                return new_so_far
            else:
                return [values]

    return recu(n, [])


forty_two = get_combos("42")
thirty_one = get_combos("31")

# There is only one combo because 0: 8 11
combos = get_combos("0")[0]

set_42 = set(forty_two)
set_31 = set(thirty_one)

# if they intersect then it gets hard!
assert len(set_42.intersection(set_31)) == 0

# Attempt 1 - stupidly complex

total = 0
for i, m in enumerate(messages):
    copy_m = m
    changed = True
    eight_found = False
    eleven_found = (False, False)
    valid = True
    while changed:
        changed = False

        found_one_31 = False
        change_31 = True
        num_31 = 0
        while change_31 and not eight_found:
            # Can end with multiple 31s
            change_31 = False
            for eleven in thirty_one:
                if copy_m.endswith(eleven):
                    copy_m = copy_m[: -len(eleven)]
                    found_one_31 = True
                    change_31 = True
                    num_31 += 1
                    eleven_found = (True, eleven_found[1])
                    break

        if not eleven_found[0]:
            # Must find at least one 31 at the end
            # If not then it is not a match
            valid = False
            break

        # Must be same number of 42s as 31s
        num_42 = 0
        change_42 = True
        while change_42 and not eight_found:
            if num_31 == 0:
                break
            change_42 = False
            for eight in forty_two:
                if copy_m.endswith(eight):
                    copy_m = copy_m[: -len(eight)]
                    eleven_found = (eleven_found[0], True)
                    change_42 = True
                    num_42 += 1
                    break
            if num_42 == num_31:
                break

        if num_42 != num_31:
            # Cannot be valid
            valid = False
            break

        if not eleven_found[1]:
            # Must find at least one 42 at the end
            # If not then it is not a match
            valid = False
            break

        for eight in forty_two:
            if copy_m.startswith(eight):
                copy_m = copy_m[len(eight) :]
                changed = True
                eight_found = True
                break

        if not eight_found:
            # Must find at least one 8
            # If not then it is not a match
            valid = False
            break

    if len(copy_m) == 0 and valid:
        # Success
        total += 1
        # print(m)

# 357
print(f"answer = {total}")

# Second attempt - much better
total = 0

for i, m in enumerate(messages):
    copy_m = m
    num_42_at_front = 0
    num_42_at_back = 0
    num_31 = 0

    changes = True
    while changes:
        changes = False

        while True:
            changed = False
            for value in forty_two:
                if copy_m.startswith(value):
                    copy_m = copy_m[len(value) :]
                    changed = True
                    num_42_at_front += 1
            if not changed:
                break

        while True:
            changed = False
            for value in thirty_one:
                if copy_m.startswith(value):
                    copy_m = copy_m[len(value) :]
                    changed = True
                    num_31 += 1
            if not changed:
                break
        if len(copy_m) == 0 and num_42_at_front > num_31 > 0:
            total += 1
            # print(m)


# 357
print(f"answer = {total}")
