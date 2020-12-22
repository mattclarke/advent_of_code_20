from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

deck_1 = []
deck_2 = []

player_2 = False

for l in puzzle_input:
    if l.startswith("Player"):
        continue
    if l == "":
        player_2 = True
        continue
    if player_2:
        deck_2.append(int(l))
    else:
        deck_1.append(int(l))

# print(deck_1)
# print(deck_2)

while deck_1 and deck_2:
    p1 = deck_1.pop(0)
    p2 = deck_2.pop(0)
    if p1 > p2:
        deck_1.append(p1)
        deck_1.append(p2)
    elif p2 > p1:
        deck_2.append(p2)
        deck_2.append(p1)
    else:
        assert False

total = 0
if deck_1:
    pts = len(deck_1)
    for card in deck_1:
        total += card * pts
        pts -= 1
else:
    pts = len(deck_2)
    for card in deck_2:
        total += card * pts
        pts -= 1

# 35005
print(f"answer = {total}")


# Part 2
deck_1 = []
deck_2 = []
player_2 = False

for l in puzzle_input:
    if l.startswith("Player"):
        continue
    if l == "":
        player_2 = True
        continue
    if player_2:
        deck_2.append(int(l))
    else:
        deck_1.append(int(l))


def solve(deck1, deck2):
    def recursion(d1, d2, game):
        seen_local = set()

        round_num = 1

        while d1 and d2:
            if str(d1) in seen_local or str(d2) in seen_local:
                # Avoids infinite loop
                return 1

            seen_local.add(str(d1))
            seen_local.add(str(d2))

            old_d1 = copy(d1)
            old_d2 = copy(d2)

            p1 = d1.pop(0)
            p2 = d2.pop(0)

            if p1 <= len(d1) and p2 <= len(d2):
                # Recurse
                res = recursion(copy(d1[:p1]), copy(d2[:p2]), game + 1)
            elif p1 > p2:
                res = 1
            else:
                res = 2

            if res == 1:
                d1.append(p1)
                d1.append(p2)
            else:
                d2.append(p2)
                d2.append(p1)

            # print("================")
            # print(f"Player 1 deck {old_d1}")
            # print(f"Player 2 deck {old_d2}")
            # print(f"Player 1 played {p1}")
            # print(f"Player 2 played {p2}")
            # print(f"Player {res} wins round {round_num} of game {game}!")
            round_num += 1
        if d1:
            return 1
        else:
            return 2

    round_num = 1
    game = 1
    seen = set()
    while deck1 and deck2:
        if str(deck1) in seen or str(deck2) in seen:
            # Avoids infinite loop
            assert False

        seen.add(str(deck1))
        seen.add(str(deck2))

        old_d1 = copy(deck1)
        old_d2 = copy(deck2)

        p1 = deck1.pop(0)
        p2 = deck2.pop(0)
        if p1 <= len(deck1) and p2 <= len(deck2):
            res = recursion(copy(deck1[:p1]), copy(deck2[:p2]), game + 1)
        elif p1 > p2:
            res = 1
        else:
            res = 2

        if res == 1:
            deck1.append(p1)
            deck1.append(p2)
        else:
            deck2.append(p2)
            deck2.append(p1)

        # print("================")
        # print(f"Player 1 deck {old_d1}")
        # print(f"Player 2 deck {old_d2}")
        # print(f"Player 1 played {p1}")
        # print(f"Player 2 played {p2}")
        # print(f"Player {res} wins round {round_num} of game {game}!")

        round_num += 1
        seen.clear()

    return deck1 if deck1 else deck2


winning_deck = solve(copy(deck_1), copy(deck_2))

total = 0

pts = len(winning_deck)
for card in winning_deck:
    total += card * pts
    pts -= 1

# 32751
print(f"answer = {total}")
