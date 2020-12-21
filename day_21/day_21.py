with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

INGREDS = []
ALLERGENS = []

all_ingreds = {}

for line in puzzle_input:
    line = line.replace("(", "").replace(")", "").replace(",", "")
    parts = line.split(" contains ")
    assert len(parts) == 2
    ingreds = {x for x in parts[0].split(" ")}
    for i in ingreds:
        num = all_ingreds.get(i, 0) + 1
        all_ingreds[i] = num
    allergens = {x for x in parts[1].split(" ")}
    INGREDS.append(ingreds)
    ALLERGENS.append(allergens)

# print(INGREDS)
# print(all_ingreds)

POSS = {}

for ings, alls in zip(INGREDS, ALLERGENS):
    for a in alls:
        poss = POSS.get(a, [])
        poss.append(ings)
        POSS[a] = poss


# Find initials candidates
for key, values in POSS.items():
    if len(values) > 1:
        base = values[0]
        for v in values:
            base = base.intersection(v)
        POSS[key] = base
    else:
        POSS[key] = values[0]

print(POSS)

SOLVED = set()

changes = True
while changes:
    changes = False
    for key, values in POSS.items():
        if len(values) == 1 and list(values)[0] not in SOLVED:
            SOLVED |= values
            changes = True
        elif len(values) > 1:
            new_v = set()
            for v in values:
                if v not in SOLVED:
                    new_v.add(v)
            if new_v != values:
                POSS[key] = new_v
                changes = True
print(POSS)
valid_ingredients = [x for x in all_ingreds if x not in SOLVED]
print(valid_ingredients)

total = 0
for v in valid_ingredients:
    total += all_ingreds[v]

# 2493
print(f"answer = {total}")


# Part 2
sorted_allegens = list(POSS.keys())
sorted_allegens.sort()

definitive_list = []

for a in sorted_allegens:
    v = POSS[a]
    definitive_list.append(list(v)[0])

answer = ",".join(definitive_list)

# kqv,jxx,zzt,dklgl,pmvfzk,tsnkknk,qdlpbt,tlgrhdh
print(f"answer = {answer}")
