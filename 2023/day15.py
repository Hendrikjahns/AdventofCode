def get_data():
    with open("input_day15.txt") as file:
        data = file.read().split(",")
    return data


def get_asciis(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def convert_steps(data):
    for i, step in enumerate(data):
        input_data[i] = step.replace("-", "=-").split("=")
        input_data[i].append(get_asciis(input_data[i][0]))
    return data


def process_steps(data2):
    box_dict = {i: {} for i in range(0, 256)}
    for step in data2:
        if step[1] != "-":
            box_dict[step[2]][step[0]] = step[1]
        else:
            if step[0] in box_dict[step[2]]:
                del box_dict[step[2]][step[0]]

    sum_focusing_power = 0
    for key in box_dict.keys():
        for count, lens in enumerate(box_dict[key].keys()):
            sum_focusing_power += (key + 1) * (count + 1) * int(box_dict[key][lens])
    return sum_focusing_power


input_data = get_data()
solution1 = 0
for line in input_data:
    solution1 += get_asciis(line)
print(f"Solution 1: {solution1}")

input_data2 = convert_steps(input_data)
solution2 = process_steps(input_data2)
print(f"Solution 2: {solution2}")
