
def main():

    # open file
    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    races = initiate_races(lines)
    race = races[0]

    winning_ways = get_winning_races(race)
    print(winning_ways)


def get_winning_races(race):

    time, distance = race

    # we could check forward and backwards
    min_hold = 0
    for hold in range(time + 1):
        time_remaining = time - hold
        distance_travelled = hold * time_remaining

        if distance_travelled > distance:
            min_hold = hold
            break

    # checking backwards
    max_hold = time
    for hold in range(time, -1, -1):
        time_remaining = time - hold
        distance_travelled = hold * time_remaining

        if distance_travelled > distance:
            max_hold = hold
            break

    return (max_hold - min_hold) + 1


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
