from pprint import pprint


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    network = initialize_network(lines)

    instructions = network.get("instructions")

    steps = 0
    instruction_index = 0
    current_node = "AAA"
    while current_node != "ZZZ":

        current_instruction = instructions[instruction_index]

        # get the left or right node based on current instruction
        if current_instruction == "R":
            current_node = network.get(current_node)[1]
        elif current_instruction == "L":
            current_node = network.get(current_node)[0]

        # if we reach the end of our instructions, reset it to the beginning
        if instruction_index >= len(instructions) - 1:
            instruction_index = 0
        else:
            instruction_index += 1

        steps += 1

    print(steps)


def initialize_network(lines):

    instructions = lines[0]
    raw_nodes = lines[2:]

    network = {}
    for node in raw_nodes:
        split = node.split("=")

        current_node, map = split

        # strip any trailing / leading whitespace
        current_node = current_node.strip()
        map = map.strip()[1:len(map) - 2].split(",")
        left_node, right_node = map

        left_node = left_node.strip()
        right_node = right_node.strip()

        network[current_node] = (left_node, right_node)

    network["instructions"] = instructions
    return network


if __name__ == "__main__":
    main()
