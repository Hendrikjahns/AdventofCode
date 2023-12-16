def get_data():
    with open("input_day9.txt") as file:
        data = [[[int(j) for j in i.split(" ")]] for i in file.read().splitlines()]
    return data


def get_extrapolated_values(data, part):
    sum_extrapolated_values = 0
    for history in data:
        current_line = history[-1]
        while not all(v == 0 for v in current_line):
            new_line = []
            for i in range(0, len(current_line) - 1):
                new_line.append(current_line[i + 1] - current_line[i])
            history.append(new_line)
            current_line = history[-1]
        sum_extrapolated_values += extrapolate_sequence(history, part)
    return sum_extrapolated_values


def extrapolate_sequence(history, part):
    if part == 2:
        history = [list(reversed(seq)) for seq in history]
    layers = len(history)
    history[-1].append(0)
    for i in range(-2, -layers - 1, -1):
        if part == 1:
            history[i].append(history[i][-1] + history[i + 1][-1])
        if part == 2:
            history[i].append(history[i][-1] - history[i + 1][-1])
    return history[0][-1]


input_data = get_data()
solution1 = get_extrapolated_values(input_data, 1)
print(f"Solution 1: {solution1}")

solution2 = get_extrapolated_values(input_data, 2)
print(f"Solution 2: {solution2}")

