from pprint import pprint
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
TYPE_STRENGTH = ["HIGH", "ONE", "TWO", "THREE", "FULL", "FOUR", "FIVE"]


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    hands = initialize_hands(lines)

    # this is a map
    hands_with_type = get_hands_with_card_type(hands)

    # sort hands in place
    for hand_with_type in hands_with_type.values():
        sort_hands_with_same_type(hand_with_type)

    # get a list of hands with sorted type and strentth
    sorted_cards = []
    for hand_type in TYPE_STRENGTH:
        if hands_with_type.get(hand_type) is None:
            continue
        else:
            sorted_cards.extend(hands_with_type.get(hand_type))

    pprint(sorted_cards)
    total = 0
    for i, hand in enumerate(sorted_cards):
        cards, bid = hand
        value = bid * (i + 1)
        total += value
    print(total)


def get_hand_value(hand, rank):
    cards, bid = hand
    return bid * rank


def sort_hands_with_same_type(hands):

    swapped = False
    # bubble sort
    for i in range(len(hands) - 1):
        for j in range(0, len(hands)-i-1):
            if hand_is_bigger(hands[j], hands[j + 1]):
                swapped = True
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
        if not swapped:
            return hands
    return hands


def hand_is_bigger(hand_one, hand_two):
    """checks if hand one is bigger than hand two, returns boolean"""
    cards_one, bid_one = hand_one
    cards_two, bid_two = hand_two

    for index, card_one in enumerate(cards_one):
        card_two = cards_two[index]

        card_one_strength = CARDS.index(card_one)
        card_two_strength = CARDS.index(card_two)

        if card_one_strength > card_two_strength:
            return True
        elif card_one_strength < card_two_strength:
            return False
        else:
            continue

    print("ERROR OCCURED")


def get_hands_with_card_type(hands):

    hands_with_type = {}

    for hand in hands:
        card_type = get_card_type(hand)

        if hands_with_type.get(card_type) is None:
            hands_with_type[card_type] = [hand]
        else:
            hands_with_type[card_type].append(hand)

    return hands_with_type


def get_card_type(hand):
    cards, bid = hand

    card_count = get_card_count(cards)

    count_pairs = 0
    index = 0
    for card, count in card_count.items():
        if count == 2:
            count_pairs += 1

        card_counts = card_count.values()
        if 5 in card_counts:
            return "FIVE"
        elif 4 in card_counts:
            return "FOUR"
        elif 3 in card_counts and 2 in card_counts:
            return "FULL"
        elif 3 in card_counts:
            return "THREE"
        elif count_pairs == 2:
            return "TWO"
        elif count_pairs == 1 and index == len(card_counts) - 1:
            return "ONE"
        index += 1

    return "HIGH"


def get_card_count(cards):
    card_count = {}
    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1
    return card_count


def initialize_hands(lines):
    hands = []
    for line in lines:
        hand, bid = line.strip().split(" ")
        bid = int(bid)
        hands.append((hand, bid))

    return hands


if __name__ == "__main__":
    main()
