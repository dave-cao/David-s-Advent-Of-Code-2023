from pprint import pprint


def main():

    with open("./input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # convert into a matrix
    matrix = []
    for line in lines:
        row = [char for char in line]
        matrix.append(row)

    # convert all our gears into tuples with an id
    gear_id = 1
    for row_i, row in enumerate(matrix):
        for col_i, char in enumerate(row):
            if char == "*":
                matrix[row_i][col_i] = (char, gear_id)
                gear_id += 1

    valid_numbers = []

    for row_i, row in enumerate(matrix):

        current_number = ""
        valid_number = False

        for col_i, element in enumerate(row):
            current_pos = (row_i, col_i)

            # convert tuples
            if type(element) is tuple:
                gear_id = element[1]
                element = element[0]

            # if we began the match, create our current number
            if element.isnumeric():
                current_number += element

                # check element
                if is_adjacent(current_pos, matrix):
                    gear_id = is_adjacent(current_pos, matrix)
                    valid_number = True
            else:
                # append the current number only if its a valid number
                if valid_number:
                    valid_numbers.append((current_number, gear_id))

                # clear current number
                current_number = ""

                # reset valid_number
                valid_number = False

        if current_number and valid_number:
            valid_numbers.append(current_number)

    number_map = {}

    # get rid of duplicates
    for number_tuple in valid_numbers:
        element, gear_id = number_tuple
        number_map[gear_id] = number_map.get(gear_id, 0) + 1

    valid_numbers_duplicates = valid_numbers.copy()
    for number_tuple in valid_numbers:
        element, gear_id = number_tuple
        if number_map.get(gear_id) == 1:
            valid_numbers_duplicates.remove(number_tuple)

    # add number ratios
    map_ratios = {}
    for number_tuple in valid_numbers_duplicates:
        element, gear_id = number_tuple
        element = int(element)

        # if the gear id has not been initialized
        if not map_ratios.get(gear_id):
            map_ratios[gear_id] = element
        else:
            map_ratios[gear_id] = map_ratios.get(gear_id) * element

    print(sum(map_ratios.values()))


def is_adjacent(current_pos, matrix):
    """Checks if the current element is a valid number"""

    row_i, col_i = current_pos

    top = (row_i - 1, col_i)
    bot = (row_i + 1, col_i)

    left = (row_i, col_i - 1)
    right = (row_i, col_i + 1)

    top_left = (row_i - 1, col_i - 1)
    top_right = (row_i - 1, col_i + 1)
    bot_left = (row_i + 1, col_i - 1)
    bot_right = (row_i + 1, col_i + 1)

    positions = [top, bot, left, right,
                 top_left, top_right, bot_left, bot_right]

    for pos in positions:
        row, col = pos

        # check if its valid positions
        is_valid_row = 0 <= row <= len(matrix) - 1
        is_valid_col = 0 <= col <= len(matrix[0]) - 1

        if is_valid_row and is_valid_col:

            # check that position
            element_to_check = matrix[row][col]

            if type(element_to_check) is tuple:
                gear_id = element_to_check[1]
                element_to_check = element_to_check[0]

            if element_to_check == "*":
                return gear_id

    return False


if __name__ == "__main__":
    main()
