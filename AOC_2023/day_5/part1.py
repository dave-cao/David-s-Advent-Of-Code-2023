from pprint import pprint
from tqdm import tqdm


def main():

    with open("inputSmall.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # initialize maps
    seed_map = initialize_maps(lines)

    # get seeds
    seeds = seed_map.get("seeds")
    seeds = [int(seed) for seed in seeds]

    location_numbers = []
    for seed in seeds:
        print("Converting seed number:", seed)
        location_numbers.append(seed_to_location(seed_map, seed))

    # convert the seeds into location numbers
    print(location_numbers)
    print("MINIMUM:", min(location_numbers))


def seed_to_location(seed_map, seed_number):

    # convert the number from a seed all the way to location
    maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
            "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    converted_number = seed_number
    for map_name in maps:
        print("Seed number", seed_number, "is being converted:", map_name)
        map = seed_map.get(map_name)
        # go through each map in order and convert the number each time
        converted_number = convert_number(map, converted_number, map_name)

    return converted_number


def convert_number(maps: str, num: int, map_name: str) -> int:
    # takes a map
    for map in maps:
        destination, source, span = map

        # convert to ints
        og_destination = int(destination)
        og_source = int(source)
        span = int(span)

        # cut down search
        if num < og_source or num > og_source + span:
            continue
        else:
            distance = og_destination - og_source
            return num + distance

    return num


def initialize_maps(lines):
    # get seeds
    seeds = lines[0].split(":")[1].split(" ")
    seeds = [seed for seed in seeds if seed]

    # separate maps
    new_map = False
    current_map_name = ""
    all_maps = {}
    for line in lines:
        line = line.split(" ")

        if new_map:
            current_map_name = line[0].strip()

        # if there is a current map, append it's details into all maps
        if current_map_name:
            if all_maps.get(current_map_name) is None:
                all_maps[current_map_name] = []
            else:
                all_maps.get(current_map_name).append(line)

        if line[0] == "":
            new_map = True
        else:
            new_map = False

    all_maps["seeds"] = seeds

    # get rid of any empty values now (needed before to distinguish new maps)
    for arr in all_maps.values():
        if arr[-1][0] == "":
            arr.pop()

    return all_maps


if __name__ == "__main__":
    main()
