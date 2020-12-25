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
Reasoning: treat as a complex number where x-axis is real and y-axis is imaginary, multiplying by i is a 90 degree rotation anti-clockwise.
```
# rotate once
x * i = ix (x is now along the imaginary axis, i.e. y) => what was originally the x component is now the y component
iy * i = -y (y is now along the real axis, i.e. x) => what was originally the y component is now the x component

# rotate again
ix * i = -x (180 degrees from original)
-y * i = -iy (180 degrees from original)

# and so on.
```
Dividing by i is a 90 degrees rotation clockwise.

See https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-ac-analysis/v/ee-multiplying-j-rotation
and https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-ac-analysis/v/ee-complex-rotation

## Day 13
### Part 1
* Simple maths, could have been done on pen and paper
### Part 2
* Basically a calculation using the Chinese Remainder Theorem.
Worked example using one of the examples:
```
Input is [17, 'x', 13, 19]
Offsets are [0, 2, 3] (ignoring the 'x')

We are basically solving '(id - offset) mod id' for all the ids
x ≡ 0 mod 17    (17 mod 17 is the same as 0 mod 17)
x ≡ 11 mod 13
x ≡ 16 mod 19

The lcm of all the modulo:
17 * 13 * 19 = 4199
In this case, all the modulo multiplied together because they are prime.

For each id we calculate the combined modulo of the other ids excluding the current id:
n_bar_0 = 4199 / 17 = 247 (same as 13 * 19)
n_bar_1 = 4199 / 13 = 323
n_bar_2 = 4199 / 19 = 221

Next we calculate the modular multiplicative inverses, u, using:
n_bar * u ≡ 1 mod id
The easy way to do this is loop increasing u from 1 until the equation is satisfied:
247 * u0 ≡ 1 mod 17 => u0 = 2
323 * u1 ≡ 1 mod 13 => u1 = 6
221 * u2 ≡ 1 mod 19 => u2 = 8

Alternatively, we can use Euler's theorem u = a ** (m - 2) % m if a is co-prime to m.
For example:
u0 = 247 ** (17 - 2) mod 17    [in Python we can do pow(247, 15, 17)]

Table of what we have so far:

id  | a  | u |
--------------
17    0    2
13    11   6
19    16   8

CRT says that the solution is:
x = (a0 * id0 * u0) + ... + (an * idn * un)

For our example:
x = (0 * 17 * 2) + (11 * 13 * 6) + (16 * 19 * 8)
x = 49606

Finally modulo it
x = 49606 mod 4199 = 3417
```
Note: CRT relies on the ids being pairwise co-primes, i.e. gcd(a, b) = 1. For example, (4, 9) is a co-prime pair.

All this information came from:
https://www.dave4math.com/mathematics/chinese-remainder-theorem/

This was useful too:
https://en.m.wikipedia.org/wiki/Modular_multiplicative_inverse

Another completely different solution from the web is to start counting up in step-size of one of the ids until it
coincides with one of the other ids then multiple the step-size by the new id then continue until it hits another id and
then multiple the step-size again and so on. I've not tried this though...

## Day 14
### Part 1
* Relatively simple, some conversion from and to binary representation
### Part 2
* Can be done via brute-force.
Using itertools' permutation generates too many repetitions so is very slow (~5 minutes).
Generating our own permutations is much quicker (< 1 second!).

## Day 15
### Part 1
* Simple looping tracking the last two times a value occurs.
### Part 2
* Using the solution from part 1 takes ~2 minutes. Must be a quicker way...
TODO: find a quicker way!

## Day 16
### Part 1
* Parsing the input to get the valid numbers and ticket information as integers then looping around to find the invalid
numbers in the tickets.
### Part 2
* Keep track of which rules are valid for each position by comparing against all valid tickets. Then loop through each
position and if it only has one valid rule then we can remove that rule from the other position until eventually all
positions only have one rule.

## Day 17
### Part 1
* Conway's game of life but in 3-D. Used itertools' permutation to get the 26 neighbours and a set for the board.
Have to recalculate min and max for each dimension after each tick - could do this during the tick though...
### Part 2
* Same but 4-D - essentially just added an extra loop. Takes ~3 seconds.

## Day 18
### Part 1
* Basic maths parser for `+`, `*`, `(` and `)` where `*` and `+` have same precedence. I used recursion on `(`
### Part 2
* `+` has precedence over `*`. Same as Part 1 but recurse on `*` as well.

## Day 19
### Part 1
* Calculated set of all possibilities and then check messages in it. Took a while to get the recursion right.
### Part 2
* First attempt I tried taking from the back until no longer possible then take from the front; it got very complicated
with lots of flags. Didn't get the right value but worked for the examples.

Went for a walk, second attempt was just to always take from the front and then check the final string was empty and that
there were more 42s removed than 31s and 31s > 0. Once I realised using `replace` rather than indexing was a stupid
mistake because it didn't just remove the first instance but all of them (d'oh!), it worked.

Used version 2 to debug version 1 - the issue was I was missing some flag checks (and that way of doing it was stupidly complex).

## Day 20
### Part 1
* Tried Ariadne's maze, very slow (~2 minutes). Used numpy for rotations etc. (is that cheating?).
* Ideas for speed-up:
    1. Cache the transformations - brings it down to ~50s
    2. Prefilter which tiles can be neighbours of each tile - combined with 1. brings it down to ~8 seconds.
### Part 2
* REMEMBER TO READ THE INSTRUCTIONS!

## Day 21
### Part 1
* Process of elimination using sets.
### Part 2
* Simple - sort the allergens and apply CSV to the ingredients in that order.

## Day 22
### Part 1
* Trivial looping and popping.
### Part 2
* Recursion was simple enough once I understood the rules, should have read the instructions more closely.

## Day 23
### Part 1
* Trivial brute force. Lists and popping and inserting. As part 2 is bigger I went back and changed it to a linked list.
### Part 2
* Takes ~25 seconds with linked list.

## Day 24
### Part 1
* Once I worked out how to manipulate x and y in a hexagon grid then it was simple. Namely, moving directly east or west
is x + 2 or x - 2 respectively, other directions are step size 1.
### Part 2
* Conway's again. I just set the grid to a max size (200 x 200) and iterated - a bit slow ~20 seconds.
Calculating the grid size on each tick brings it down to < 2 seconds. Turns out 200 x 200 is excessive, 110 x 110 would
have been okay (~6 seconds).

## Day 25
### Part 1
* Looping!
