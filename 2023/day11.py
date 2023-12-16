import itertools


def get_data():
    with open("input_day11.txt") as file:
        data = [list(i) for i in file.read().splitlines()]
    return data


def expand_universe(data):
    y_exp, x_exp = [], []
    for y, line in enumerate(data):
        if set(line) == {"."}:
            y_exp.append(y)

    for x, col in enumerate(data[0]):
        column = []
        for y, line in enumerate(data):
            column.append(data[y][x])
        if set(column) == {"."}:
            x_exp.append(x)

    galaxies = []
    for y, row in enumerate(data):
        for x, col in enumerate(data[0]):
            if data[y][x] == "#":
                galaxies.append((x, y))

    return y_exp, x_exp, galaxies


def get_distances(galaxies, y_exp, x_exp, expansion):
    galaxy_combinations = list(itertools.combinations(galaxies, 2))
    sum_manhattan_dist = 0
    for combination in galaxy_combinations:
        count_y_exp, count_x_exp = 0, 0
        for x in x_exp:
            if min(combination[0][0], combination[1][0]) < x < max(combination[0][0], combination[1][0]):
                count_y_exp += 1
        for y in y_exp:
            if min(combination[1][1], combination[0][1]) < y < max(combination[1][1], combination[0][1]):
                count_x_exp += 1

        manhattan_distance = abs(combination[0][0] - combination[1][0]) + count_x_exp * expansion + abs(combination[1][1] - combination[0][1]) + count_y_exp * expansion
        sum_manhattan_dist += manhattan_distance
    return sum_manhattan_dist


input_data = get_data()
y_expansions, x_expansions, list_galaxies = expand_universe(input_data)

solution1 = get_distances(list_galaxies, y_expansions, x_expansions, 1)
print(f"Solution 1: {solution1}")
solution2 = get_distances(list_galaxies, y_expansions, x_expansions, 1_000_000-1)
print(f"Solution 2: {solution2}")
