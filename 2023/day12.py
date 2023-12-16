from itertools import product


def get_data():
    with open("input_day12.txt") as file:
        data = [[list(i.split(" ")[0]), [int(j) for j in i.split(" ")[1].split(",")]] for i in file.read().splitlines()]
    return data


def brute_force_springs(data):
    sum_count = 0
    for line in data:
        count_combinations = get_combinations(line)
        sum_count += count_combinations
    return sum_count


def get_combinations(line):
    count_combinations = 0
    index_unknown = [i for i, record in enumerate(line[0]) if record == "?"]
    spring_count = len(index_unknown)
    combos = set(list(product([".", "#"], repeat=spring_count)))
    for combo in combos:
        for i, index in enumerate(index_unknown):
            line[0][index] = combo[i]
        line_groups = [j for j in "".join(line[0]).split(".") if j != ""]
        line_groups = [j.count("#") for j in line_groups]
        if line_groups == line[1]:
            count_combinations += 1
    return count_combinations


input_data = get_data()
print(input_data)
solution1 = brute_force_springs(input_data)
print(f"Solution 1: {solution1}")
