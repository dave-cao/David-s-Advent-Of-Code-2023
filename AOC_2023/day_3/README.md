---
created: 2023-12-05T12:03
updated: 2023-12-05T19:24
---

## Day 3 of Advent of Code

#### Part 1
This one took a while for me to figure out. I basically had to create a matrix where each line was a row and each char was a column. From there, I had a look-up function for each character to check for symbols in all directions. If there was a symbol, then append that card into a list. At the end, we can just sum them all up together.

#### Part 2
Part 2 was a bit easier from part 1 just because it built off of what I already wrote. I just converted each gear into a tuple of element and gear id. Then whatever number was adjacent to that gear was placed into a list with the number and gear id as a tuple. From there, I got rid of any non-duplicates and multiplied similar gear numbers together. Got the sum and we get our answer.
