from pprint import pprint


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    points = [get_points(line) for line in lines]
    print(sum(points))


def get_points(line):

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

    exponent_value = my_winning_numbers - 1

    points = 0
    if exponent_value >= 0:
        points = 2 ** exponent_value

    return points


if __name__ == "__main__":
    main()
