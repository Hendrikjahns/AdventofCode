def get_data():
    with open("input_day3.txt") as file:
        data = [list(line) for line in file.read().splitlines()]
        data.insert(0, ["." for i in range(0, len(data[0]))])
        data.append(["." for i in range(0, len(data[0]))])

        for count, line in enumerate(data):
            line.append(".")
            line.insert(0, ".")
            data[count] = line

        symbols = []
        for line in data:
            for char in set(line):
                if char not in symbols and not char.isdigit() and char != ".":
                    symbols.append(char)

    return data, symbols


def get_part_numbers(data, symbols):
    part_numbers = []
    sum_gear_ratio = 0
    for y in range(1, len(data) - 2):
        for x in range(1, len(data[y]) - 2):
            if data[y][x] in symbols:
                adjacent_numbers, gear_ratio = check_number_adjacency(data, x, y)
                sum_gear_ratio += gear_ratio
                for num in adjacent_numbers:
                    if num not in part_numbers:
                        part_numbers.append(num)
    return part_numbers, sum_gear_ratio


def check_number_adjacency(data, x, y):
    adjacencies = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    adjacent_numbers = []
    gears = []
    gear_ratio = 0
    for dx, dy in adjacencies:
        if data[y + dy][x + dx].isdigit():
            number, num_start = get_num(data[y + dy], x + dx)
            part_number = [data[y][x], x, y, number, num_start, y + dy]
            if part_number not in adjacent_numbers:
                adjacent_numbers.append(part_number)
                if data[y][x] == "*":
                    gears.append(part_number)

    if len(gears) == 2:
        gear_ratio = gears[0][3] * gears[1][3]
    return adjacent_numbers, gear_ratio


def get_num(line, x):
    num_pos = []
    num_start, num_end = x, x
    for dx in [-1, 1]:
        ddx = dx
        while 0 < x + ddx < len(line):
            if line[x + ddx].isdigit():
                num_start = min(num_start, x + ddx)
                num_end = max(num_end, x + ddx)
            else:
                break
            ddx += dx

    number = int("".join(line[num_start:num_end+1]))
    return number, num_start


input_data, symbol_list = get_data()
list_part_numbers, solution_2 = get_part_numbers(input_data, symbol_list)
solution_1 = sum([i[3] for i in list_part_numbers])
print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}")
