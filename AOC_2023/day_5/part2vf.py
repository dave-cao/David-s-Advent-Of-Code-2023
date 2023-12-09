from pprint import pprint
from tqdm import tqdm

SEED_MAP_ORDER = ["soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
                  "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # initialize the map
    maps = initialize_maps(lines)

    # get seed ranges
    seed_ranges = get_seed_ranges(maps.get("seeds"))

    print("Seed ranges to parse through:", seed_ranges)

    # for each seed range
    # get its location range
    lowest_location = float("inf")
    for seed_range in (seed_ranges):

        print("Current seed range:", seed_range)
        location_ranges = get_seed_to_location_range(seed_range, maps)

        lowest_location_for_seed = get_lowest_location(location_ranges)

        if lowest_location_for_seed < lowest_location and lowest_location_for_seed != 0:
            lowest_location = lowest_location_for_seed

        print("Current lowest:", lowest_location_for_seed)

    print("LOWEST:", lowest_location)


def get_lowest_location(location_ranges):

    lowest = float("inf")

    for location in location_ranges:
        start, end = location
        if start < lowest:
            lowest = start

    return lowest


def get_seed_to_location_range(seed_range, maps):

    # get seed to soil
    seed_to_soil = get_destination_ranges_from_map(
        seed_range, maps.get("seed-to-soil"), "seed-to-soil")

    # start with the ranges we get from seed to soil
    start_ranges = seed_to_soil

    if not seed_to_soil:
        start_ranges = [seed_range]

    # convert through maps
    for map_name in SEED_MAP_ORDER:

        # TODO: DONT TAKE IN CHOPPED OFF AT LAST ONE

        new_ranges = get_destination_ranges_from_nested_array(
            start_ranges, maps.get(map_name), map_name)
        start_ranges = new_ranges

    return start_ranges


def get_destination_ranges_from_nested_array(ranges_to_convert, seed_map, map_name):
    converted_ranges = []
    for s_range in ranges_to_convert:
        new_ranges = get_destination_ranges_from_map(
            s_range, seed_map, map_name)

        # if we can't convert anything, pass it down
        if not new_ranges:
            converted_ranges.append(s_range)
        else:
            converted_ranges.extend(new_ranges)

    return converted_ranges


def get_destination_ranges_from_map(seed_range, seed_map, map_name):
    seed_start, seed_end = seed_range
    ranges = []
    for map in seed_map:
        destination, source, span = map

        map_start = source
        map_end = source + span

        new_range_start = -1
        new_range_end = -1

        left_start = -1
        left_end = -1

        right_start = -1
        right_end = -1

        valid_seed_start = map_start <= seed_start <= map_end
        valid_seed_end = map_start <= seed_end <= map_end

        # case where range is within map range
        if valid_seed_start and valid_seed_end:
            new_range_start = seed_start
            new_range_end = seed_end
        elif not valid_seed_start and valid_seed_end:
            # chops off left end
            new_range_start = map_start
            new_range_end = seed_end

            left_start = seed_start
            left_end = map_start - 1

        elif valid_seed_start and not valid_seed_end:
            # chops off right end
            new_range_start = seed_start
            new_range_end = map_end

            right_start = map_end + 1
            right_end = seed_end

        elif seed_start < map_start and seed_end > map_end:
            # take into account chopping both ends
            new_range_start = map_start
            new_range_end = map_end

            left_start = seed_start
            left_end = map_start - 1

            right_start = map_end + 1
            right_end = seed_end
        else:
            # otherwise, we are out of range
            # in this case, just return what we have
            continue

        # DON'T PASS DOWN CHOPPED RANGES AT THE END
        if left_start != -1:
            ranges.append((left_start, left_end))

        # convert source range into destination range
        distance = destination - source
        ranges.append((new_range_start + distance, new_range_end + distance))

        if right_start != -1:
            ranges.append((right_start, right_end))

    return ranges


def get_seed_ranges(seeds):

    seed_pairs = []
    seed_start = 0
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            seed_start = seed
        else:
            seed_range = seed
            seed_pairs.append((seed_start, seed_start + seed_range))
    return seed_pairs


def initialize_maps(lines):
    # get seeds
    seeds = lines[0].split(":")[1].split(" ")
    seeds = [int(seed) for seed in seeds if seed]

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

    # get rid of any empty values now (needed before to distinguish new maps)
    for arr in all_maps.values():
        if arr[-1][0] == "":
            arr.pop()

    # turn all values into numbers
    for arr in all_maps.values():
        for inner in arr:
            for i, element in enumerate(inner):
                inner[i] = int(inner[i])

    all_maps["seeds"] = seeds
    return all_maps


if __name__ == "__main__":
    main()
