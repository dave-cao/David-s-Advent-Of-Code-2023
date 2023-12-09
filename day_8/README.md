

## Advent of Code Day 8

### Part 1:
This question was simple enough, just continue on looking through the network that they gave us and eventually you get an answer.

### Part 2:
This one was the tricky one. I basically had to intuitively guess that a starting node with **n** steps will go back to *z* in **n x 2** steps, **n x 3** steps etc. Basically it is a cycle. From there, if we can get the cycle for each, then we can get the LOWEST COMMON MULTIPLE of all the numbers and we can get our answer. Otherwise, it will take forever to loop through everything. 

There was no way I could have figured that question out by myself. I basically looked at some hints from reddit and they pointed me towards looking at LCM for a solution. From there, I did some experimenting on my steps and numbers (hence the **dig** method), to finally realize how to solve this.
