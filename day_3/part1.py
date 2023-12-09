

def main():

    with open("./input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # convert into a matrix
    matrix = []
    for line in lines:
        row = [char for char in line]
        matrix.append(row)

    valid_numbers = []

    for row_i, row in enumerate(matrix):

        current_number = ""
        valid_number = False

        for col_i, element in enumerate(row):
            current_pos = (row_i, col_i)

            # if we began the match, create our current number
            if element.isnumeric():
                current_number += element

                # check element
                if is_adjacent(current_pos, matrix):
                    valid_number = True
            else:
                # append the current number only if its a valid number
                if valid_number:
                    valid_numbers.append(current_number)

                # clear current number
                current_number = ""

                # reset valid_number
                valid_number = False

        if current_number and valid_number:
            valid_numbers.append(current_number)

    int_numbers = [int(number) for number in valid_numbers]
    print(sum(int_numbers))


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
            if not element_to_check.isnumeric() and element_to_check != ".":
                return True

    return False


if __name__ == "__main__":
    main()
