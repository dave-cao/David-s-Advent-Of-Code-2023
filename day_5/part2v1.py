from pprint import pprint
from tqdm import tqdm


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # initialize maps
    seed_map = initialize_maps(lines)

    # # get seeds
    print("Getting seeds...")

    # # write seeds to file to save memory
    get_seeds(seed_map.get("seeds"), seed_map.get("seed-to-soil"), seed_map)


def get_seeds(seeds, seed_to_soil, seed_map):

    seeds = [int(seed) for seed in seeds]

    # get range from seed to soil map
    min_range = float('inf')
    max_range = 0
    for map in seed_to_soil:
        destination, source, seed_range = map

        source = int(source)
        seed_range = int(seed_range)

        max = source + seed_range
        min = source

        # grab the max and min ranges
        if max > max_range:
            max_range = max

        if min < min_range:
            min_range = min

    start_seed = 0
    seed_pairs = []
    for i, seed in enumerate(seeds):
        # if its even, then it is a starting seed point
        if i % 2 == 0:
            start_seed = seed
        else:
            # if it is odd, then it is a range
            range_seed = seed
            seed_pairs.append((start_seed, range_seed))

    lowest_location = float("inf")
    for index, pair in enumerate(seed_pairs):
        # check if pair is within range

        start_seed, range_seed = pair
        end_seed = start_seed + range_seed

        print("Getting seed pair:", pair, f"{index}/{len(seed_pairs)}")
        for i in tqdm(range(start_seed, end_seed)):
            if i > max_range:
                break
            if i < min_range:
                continue

            # only get the seeds that are relevant
            if i >= min_range and i <= max_range:

                location = seed_to_location(seed_map, i)

                if location < lowest_location:
                    lowest_location = location

        print("The current lowest location is:", lowest_location)

    print("The lowest location is:", lowest_location)


def seed_to_location(seed_map, seed_number):

    # convert the number from a seed all the way to location
    maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
            "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    converted_number = seed_number
    for map_name in maps:
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
