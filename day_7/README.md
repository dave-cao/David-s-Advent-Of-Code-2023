---
created: 2023-12-07T15:55
updated: 2023-12-07T15:55
---


## Advent of Code Day 7

### Thoughts After Completion

- This wasn't bad, I just had to make a bunch of smaller functions and seperate each task. Both part 1 and part 2 were linked to each other so I only needed to change one function to get part 2. The problem was that there were more edge cases to part 2 then I thought which made me take a lot more time.


Instructions

- We are given a list of hands consisting of 5 cards each
- We have to find the strength of each hand

Every hand is exactly one type. From strongest to weakest, they are:

## ORDER BY TYPE FIRST

- Five of a kind, where all five cards have the same label: AAAAA
- Four of a kind, where four cards have the same label and one card has a different label: AA8AA
- Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
- Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
- Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
- One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
- High card, where all cards' labels are distinct: 23456


## ORDER BY STRONGEST FIRST CARD SECOND (if same type)
- continue to the second, third, fourth... etc if the card is the same

For our inputs:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```
First Part: Hand
Second Part: bid amount

Each hand wins an amount equal to its bid multiplied by its rank

Potential functions needed:
```python

def get_type(card: str) -> str:
    """Gets the type of the card"
    pass

def get_stronger_card(card_one, card_two):
    pass
```

1. we need to get the type of the card
2. do it for all the cards
3. perhaps have a map that has a list of all the types of cards
4. sort the similar card type by strength

