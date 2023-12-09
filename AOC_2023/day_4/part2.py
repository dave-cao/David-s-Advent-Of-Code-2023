from pprint import pprint


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    card_map = {}
    for line in lines:

        # grab the card_id from the line
        card_id_string, card_numbers = line.split(":")
        card_id_string = card_id_string.strip()

        raw_card_id = card_id_string.split(" ")
        raw_card_id = [card for card in raw_card_id if card]
        _, card_id = raw_card_id
        card_id = int(card_id)

        # put original instance of card within map
        card_map[card_id] = card_map.get(card_id, 0) + 1

        # get the points of the current line
        points = get_matching_number(line)

        # get current cards already with the current id
        iterations = card_map[card_id]

        # add cards based no how many iterations of the card we already have
        for _ in range(iterations):
            # get copies of the cards based on the points taken
            for i in range(points):
                card_to_copy_id = card_id + (i + 1)

                # don't go over range
                if card_to_copy_id <= len(lines):
                    card_map[card_to_copy_id] = card_map.get(
                        card_to_copy_id, 0) + 1

    print(card_map)
    print(sum(card_map.values()))


def get_matching_number(line):

    card_id, card_numbers = line.split(":")
    winning_numbers, my_numbers = card_numbers.split("|")

    winning_numbers = winning_numbers.split(" ")
    my_numbers = my_numbers.split(" ")

    winning_numbers = [num for num in winning_numbers if num]
    my_numbers = [num for num in my_numbers if num]

    my_winning_numbers = 0
    for number in my_numbers:
        if number in winning_numbers:
            my_winning_numbers += 1

    return my_winning_numbers


if __name__ == "__main__":
    main()
