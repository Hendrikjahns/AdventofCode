def get_data():
    with open("input_day1.txt") as file:
        data = file.read().splitlines()
    return data


def get_calibration_values(data, version):
    num_dict = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n",
                "eight": "e8t", "nine": "n9e"}
    sum_cal_values = 0

    for i, _ in enumerate(data):
        if version == 2:
            for key in num_dict.keys():
                data[i] = data[i].replace(key, num_dict[key])

        data[i] = [int(x) for x in list(data[i]) if x.isdigit()]
        cal_value = int(str(data[i][0]) + str(data[i][-1]))
        sum_cal_values += cal_value

    return sum_cal_values


input_data = get_data()
solution_1 = get_calibration_values(input_data, 1)
print(f"Solution 1: {solution_1}")

input_data = get_data()
solution_2 = get_calibration_values(input_data, 2)
print(f"Solution 2: {solution_2}")








