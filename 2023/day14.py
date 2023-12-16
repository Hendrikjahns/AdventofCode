def get_data():
    with open("input_day14.txt") as file:
        data = [list(i) for i in file.read().splitlines()]
    return data


def tilt_dish(data):
    for line in range(1, len(data)):
        for i, tile in enumerate(data[line]):
            if tile == "O":
                j = 0
                while data[line - j - 1][i] == "." and line - j > 0:
                    j += 1
                data[line - j][i] = "O"
                if j > 0:
                    data[line][i] = "."
    return data


def get_load(data):
    total_load = 0
    for i, line in enumerate(data):
        line_load = line.count("O") * (len(data) - i)
        total_load += line_load
    return total_load


input_data = get_data()
tilted_dish = tilt_dish(input_data)
solution1 = get_load(tilted_dish)
print(f"Solution 1: {solution1}")

input_data = get_data()
for k in range(0, 1000):
    for l in range(0, 4):
        input_data = tilt_dish(input_data)
        input_data = list(map(list, zip(*reversed(input_data))))

solution2 = get_load(input_data)
print(f"Solution 2: {solution2}")
