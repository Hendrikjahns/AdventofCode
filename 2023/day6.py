def get_data():
    with open("input_day6.txt") as file:
        data_time, data_distance = file.read().split("\n")
        data_time = [int(i) for i in data_time.split(" ")[1:] if i != ""]
        data_distance = [int(i) for i in data_distance.split(" ")[1:] if i != ""]
    return data_time, data_distance


def get_record_combinations(times, distances):
    record_combinations_mult = 1
    for time, distance in zip(times, distances):
        record_combinations = 0
        for race_time in range(0, time+1):
            charge_time = time - race_time
            achieved_distance = race_time * charge_time
            if achieved_distance > distance:
                record_combinations += 1
        record_combinations_mult *= record_combinations
    return record_combinations_mult


input_data_time, input_data_distance = get_data()
solution1 = get_record_combinations(input_data_time, input_data_distance)
print(f"Solution 1: {solution1}")

input_data_distance = [str(j) for j in input_data_distance]
input_data_time = [str(j) for j in input_data_time]
input_data_distance = [int("".join(input_data_distance))]
input_data_time = [int("".join(input_data_time))]
solution2 = get_record_combinations(input_data_time, input_data_distance)
print(f"Solution 2: {solution2}")
