def get_data():
    with open("input_day5.txt") as file:
        data = file.read()
    seeds_part1 = [int(i) for i in data.splitlines()[0][7:].split(" ")]
    seeds_part2 = [[seeds_part1[i], seeds_part1[i+1]] for i in range(0, len(seeds_part1)-1, 2)]
    maps = [j.splitlines() for j in data.split("\n\n")[1:]]
    for count, map in enumerate(maps):
        maps[count] = [map[0].replace(" map:", ""), [[int(l) for l in k.split(" ")] for k in map[1:]]]
    return seeds_part1, seeds_part2, maps


def find_lowest_location_part1(seeds, maps):
    lowest_location = 1_000_000_000_000_000
    for seed in seeds:
        start = seed
        for map in maps:
            print("start:", start)
            start = check_map(start, map)
        if start < lowest_location:
            lowest_location = start
    return lowest_location


def find_lowest_location_part2(seeds, maps):
    lowest_location = 1_000_000_000_000_000
    for seed_range in seeds:
        print(seed_range[0], seed_range[0] + seed_range[1])
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            start = seed
            for map in maps:
                start = check_map(start, map)

            if start < lowest_location:
                lowest_location = start
    return lowest_location


def check_map(start, map):
    start_out = None
    for map_range in map[1]:
        if map_range[1] < start < map_range[1] + map_range[2]:
            index_start = start - map_range[1]
            start_out = map_range[0] + index_start
            print(start_out)

    if start_out is None:
        start_out = start
    return start_out


seeds_list_part1, seeds_list_part2, maps_list = get_data()

solution1 = find_lowest_location_part1(seeds_list_part1, maps_list)
print(f"Solution 1: {solution1}")

print(seeds_list_part2)
solution2 = find_lowest_location_part2(seeds_list_part2, maps_list)
print(f"Solution 2: {solution2}")