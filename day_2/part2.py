def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.rstrip() for line in lines]

    total = 0
    for line in lines:
        total += get_min_power(line)

    print(total)


def get_min_power(line: str):

    # store max values of each colour
    max_red = 0
    max_blue = 0
    max_green = 0

    # split text into game id and game
    game_id, game = line.split(":")

    # extract just the game sets
    game_sets = game.split(";")

    # for each game set
    for game_set in game_sets:
        game_set = game_set.strip()

        cubes = game_set.split(",")

        for cube in cubes:
            cube = cube.strip()

            amount, colour = cube.split(" ")
            amount = int(amount)

            if colour == "red" and max_red < amount:
                max_red = amount
            if colour == "blue" and max_blue < amount:
                max_blue = amount
            if colour == "green" and max_green < amount:
                max_green = amount

    return max_red * max_blue * max_green


if __name__ == "__main__":
    main()
