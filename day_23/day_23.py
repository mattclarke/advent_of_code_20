from copy import copy

PUZZLE_INPUT = "538914762"

# PUZZLE_INPUT = "389125467"

puzzle_input = [int(x) for x in PUZZLE_INPUT]
# print(puzzle_input)

cups = puzzle_input[:]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def as_list(self):
        result = [self.value]
        node = self.next
        while node and node != self:
            result.append(node.value)
            node = node.next
        return result


linked_list = None
last = None
lookup = {}

for c in puzzle_input[:]:
    if linked_list:
        node = Node(c)
        last.next = node
        last = node
        lookup[c] = node
    else:
        linked_list = Node(c)
        last = linked_list
        lookup[c] = last

# Join the circle
last.next = linked_list

print(linked_list.as_list())

top_cup = linked_list
current_cup = linked_list
max_cup = max(puzzle_input)

for i in range(100):
    # print(f"\n-- move {i + 1} --")
    # print(f"cups: {top_cup.as_list()}")

    # Remove three cups
    head = current_cup.next
    tail = head.next.next
    current_cup.next = tail.next
    tail.next = None
    picked_up = [head.value, head.next.value, head.next.next.value]

    destination = current_cup.value - 1
    destination = destination if destination > 0 else max_cup
    while destination in picked_up:
        destination -= 1
        if destination < 1:
            destination = max_cup

    # print(f"current cup: {current_cup.value}")
    # print(f"pick up: {head.as_list()}")
    # print(f"destination: {destination}")

    # Insert at destination
    dest = lookup[destination]
    dest_next = dest.next
    dest.next = head
    tail.next = dest_next

    current_cup = current_cup.next

print(f"{linked_list.as_list()}")

next_node = lookup[1].next
result = []

while next_node != lookup[1]:
    result.append(str(next_node.value))
    next_node = next_node.next

# 54327968
print(f"answer = {''.join(result)}")


# Part 2
# Almost exactly the same code!
linked_list = None
last = None
lookup = {}

for c in cups:
    if linked_list:
        node = Node(c)
        last.next = node
        last = node
        lookup[c] = node
    else:
        linked_list = Node(c)
        last = linked_list
        lookup[c] = last

for i in range(len(cups)+1, 1_000_000 + 1):
    node = Node(i)
    last.next = node
    last = node
    lookup[i] = node

# Join the circle
last.next = linked_list

top_cup = linked_list
current_cup = linked_list

max_cup = 1_000_000

for i in range(10_000_000):
    # Remove three cups
    head = current_cup.next
    tail = head.next.next
    current_cup.next = tail.next
    tail.next = None
    picked_up = [head.value, head.next.value, head.next.next.value]

    destination = current_cup.value - 1
    destination = destination if destination > 0 else max_cup
    while destination in picked_up:
        destination -= 1
        if destination < 1:
            destination = max_cup

    # Insert at destination
    dest = lookup[destination]
    dest_next = dest.next
    dest.next = head
    tail.next = dest_next

    current_cup = current_cup.next

next_node = lookup[1].next
result = next_node.value * next_node.next.value

# 157410423276
print(f"answer = {result}")

