
def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    sequences = [parse_line(line) for line in lines]

    part_one(sequences)
    part_two(sequences)


def part_one(sequences):
    total = 0
    for sequence in sequences:
        total += get_next_value(sequence)

    print("PART 1:", total)


def part_two(sequences):
    total = 0
    for sequence in sequences:
        total += get_previous_value(sequence)
    print("PART 2:", total)


def get_previous_value(sequence):
    differences = get_all_differences(sequence)
    previous_value = 0
    for i in range(len(differences) - 2, -1, -1):
        value_to_subtract = differences[i][0]
        resulting_number = value_to_subtract - previous_value

        previous_value = resulting_number

    return previous_value


def get_next_value(sequence):
    differences = get_all_differences(sequence)
    next_value = 0
    for i in range(len(differences) - 2, -1, -1):
        value_to_add = differences[i][len(differences[i]) - 1]
        resulting_number = value_to_add + next_value

        next_value = resulting_number
    return next_value


def get_all_differences(sequence):
    """Gets all the differences of a single sequence"""
    # starting sequence

    difference_sequence = get_differences(sequence)
    all_sequences = [sequence, difference_sequence]
    while not has_all_zeros(difference_sequence):
        difference_sequence = get_differences(difference_sequence)
        all_sequences.append(difference_sequence)

    return all_sequences


def has_all_zeros(sequence):
    """Goes through all the values of a sequence and checks if all of it has zeros"""
    if all([value == 0 for value in sequence]):
        return True
    else:
        return False


def get_differences(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        current_value = sequence[i]
        next_value = sequence[i + 1]

        differences.append(next_value - current_value)

    return differences


def parse_line(line: str) -> list:

    raw_numbers = line.split(" ")
    raw_numbers = [int(number.strip()) for number in raw_numbers if number]
    return raw_numbers


if __name__ == "__main__":
    main()
