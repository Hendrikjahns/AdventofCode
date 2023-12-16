import math


def get_data():
    with open("input_day8.txt") as file:
        instructions, data = file.read().split("\n\n")
        data = {line.split(" = ")[0]: line.split(" = ")[1].strip("()").split(", ") for line in data.splitlines()}
        instructions = list(instructions)
    return instructions, data


def count_steps_part1(start, end, interval, instructions, data):
    current_step = start
    direction = {"R": 1, "L": 0}
    step_count = 0
    while current_step[interval:] != end:
        for instruction in instructions:
            step_count += 1
            current_step = data[current_step][direction[instruction]]
    return step_count


def count_steps_part2(instructions, data):
    nodes = [key for key in data.keys() if key[2] == "A"]
    step_counts = []
    for node in nodes:
        step_counts.append(count_steps_part1(node, "Z", 2, instructions, data))
    step_counts = math.lcm(*step_counts)
    return step_counts


input_instructions, input_data = get_data()
solution1 = count_steps_part1("AAA", "ZZZ", 0, input_instructions, input_data)
print(f"Solution 1: {solution1}")
solution2 = count_steps_part2(input_instructions, input_data)
print(f"Solution 2: {solution2}")
