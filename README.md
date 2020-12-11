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
* Variation to neighbours rule. Brute forced to go continuously in a direction until it hits something relevant.


