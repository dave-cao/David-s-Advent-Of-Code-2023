def main():

    # open file
    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    races = initiate_races(lines)

    # Part 1
    total = 1
    for race in races:
        winning_holds = get_winning_holds(race)
        total *= len(winning_holds)

    print(total)


def get_winning_holds(race):

    time, distance = race

    winning_holds = []
    for hold in range(time + 1):
        time_remaining = time - hold
        resulting_distance = hold * time_remaining

        if resulting_distance > distance:
            winning_holds.append(hold)

    return winning_holds


def initiate_races(lines):
    """Will output a list tuples of (time, distance)"""

    raw_time, raw_distance = lines

    time_numbers = raw_time.split(":")[1].strip()
    distance_numbers = raw_distance.split(":")[1].strip()

    time_numbers = time_numbers.split(" ")
    time_numbers = [int(time) for time in time_numbers if time]

    distance_numbers = distance_numbers.split(" ")
    distance_numbers = [int(distance)
                        for distance in distance_numbers if distance]

    races = []
    for i, time in enumerate(time_numbers):
        distance = distance_numbers[i]
        races.append((time, distance))

    return races


if __name__ == "__main__":
    main()
