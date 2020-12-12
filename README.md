# Advent of Code 2020
https://adventofcode.com/2020

## Day 1
### Part 1 & 2
* Simple looping and calculation.

## Day 2
### Part 1 & 2
* String parsing and simple value comparison.

## Day 3
### Part 1 & 2
* Simple looping and counting.

## Day 4
### Part 1 & 2
* Checking validity of values.

## Day 5
### Part 1
* Binary search(-ish).
### Part 2
* Finding missing value in range.

## Day 6
### Part 1
* Simple looping and tracking answers.
### Part 2
* Similar to part 1 but I made as mistake in not counting the "last group" correctly when coming out of the loop, so wasted 15 minutes.
Copy and paste error essentially.

## Day 7
### Part 1
* Use a dictionary to create a bag hierarchy then find which bags can contain "shiny gold" directly then find which bags
can contain them and so on using a queue.
### Part 2
* Similar but starting from "shiny gold" see what bags it contains and then what they contain and so on.

## Day 8
### Part 1
* Simple "machine code" device with three simple instruction types. Decode the instructions and look for the same
instruction being called twice.
### Part 2
* Iterate and replace only one nop with jmp or vice versa and check for an infinite loop (failure) or for it to reach the end of
the instruction set (success).

## Day 9
### Part 1
* Simple loop with sliding window of values.
### Part 2
* Simple double loop to create a "growing window" for each value until answer found.

## Day 10
### Part 1
* Sort then count the differences between values, plus an extra 3 for the "adaptor".
### Part 2
* The number of ways to a node is the sum of the number of ways to the previous nodes that can reach it.
Simple really but I got somewhat lost so it took longer than it should :(

## Day 11
### Part 1
* Variation on Conway's GoL. To make counting neighbours easier I put an empty border around the board.
### Part 2
* Variation to neighbours rule. Brute-forced to go continuously in a direction until it hits something relevant.

## Day 12
### Part 1
* Instructions are simple enough to deal with. Brute-forced the rotations.
### Part 2
* Rotation becomes more a bit complex, not helped by the fact I chose north to be negative. Rotation can probably be done
more elegantly.

For part 1, we can do directions like this (every year I forget this trick!):
```
# Direction is a number (0,1,2,3)
# 0 = north, 1 = east, 2 = south, 3 = west
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# rotation right is then
dir = (dir + 1) % 4

# rotation left is:
dir = (dir + 3) % 4
# (dir - 1) % 4 also works in Python, some languages (notably JavaScript) are different with regards to negatives:
#
# Python: -1 % 4 = 3    # (x % y = x - (y * floor(x/y)), for -2.3 floor gives -3)
# JS: -1 % 4 = -1       # (x % y = x - (y * trunc(x/y)), for -2.3 trunc gives -2)
#
# Python: 4 % -3 = -2
# JS: 4 % -3 = 1
```

For part 2, more elegant rotation is (assuming north is positive):
```
# for clockwise:
wp_x, wp_y = wp_y, -wp_x

# for anti-clockwise:
wp_x, wp_y = -wp_y, wp_x
```
Reasoning: treat as a complex number where x-axis is real and y-axis is imaginary, multiplying by i is a 90 degree rotation.
```
# rotate once
x * i = ix (x is now along the imaginary axis, i.e. y) => what was originally the x component is now the y component
iy * i = -y (y is now along the real axis, i.e. x) => what was originally the y component is now the x component

# rotate again
ix * i = -x (180 degrees from original)
-y * i = -iy (180 degrees from original)

# and so on.
```
See https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-ac-analysis/v/ee-multiplying-j-rotation


## Day 13
### Part 1
*
### Part 2
*
