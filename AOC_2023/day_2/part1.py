CUBE_COLOURS = ["blue", "red", "green"]
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.rstrip() for line in lines]

    total = 0
    for index, line in enumerate(lines):

        game_id = index + 1

        if is_valid_game(line):
            total += game_id

    print(total)


def is_valid_game(line):
    """Checks if the game is a valid game given a string line"""

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

            if colour == "red" and amount > MAX_RED:
                return False

            if colour == "green" and amount > MAX_GREEN:
                return False

            if colour == "blue" and amount > MAX_BLUE:
                return False

    return True


if __name__ == "__main__":
    main()
