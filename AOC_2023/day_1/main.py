
NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# this function will filter out the first and last numbers of a string


def main():

    filename = "input.txt"
    with open(filename, "r") as file:
        data = file.readlines()

    # get rid of \n at end of each line
    data = [line.rstrip() for line in data]

    values = [extract_nums_from_line(line) for line in data]

    total = sum(values)
    print(total)
    # extract_nums_from_line("eightwothree")
    # extract_nums_from_line("abcone2threexyz")

    return


def extract_nums_from_line(line: str):
    first_num = extract_num_from_line(line, False)
    last_num = extract_num_from_line(line, True)

    return int(str(first_num) + str(last_num))


def extract_num_from_line(line: str, last: bool):

    current_number = ""
    # for each number
    for number in NUMBERS:

        for i in range(len(line)):
            for q in range(i, len(line)):
                str_to_test = line[i:q + 1]

                if str_to_test in NUMBERS or str_to_test.isnumeric():
                    current_number = str_to_test
                    break

            if (str_to_test in NUMBERS or str_to_test.isnumeric()) and not last:
                break

        if (str_to_test in NUMBERS or str_to_test.isnumeric()) and not last:
            break

    if current_number.isnumeric():
        return int(current_number)
    else:
        return NUMBERS.get(current_number)


if __name__ == "__main__":
    main()
