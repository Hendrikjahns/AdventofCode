def get_data():
    with open("input_day13.txt") as file:
        data = [i.splitlines() for i in file.read().split("\n\n")]
    return data


def check_mirrors(pattern):
    max_line = len(pattern) - 1
    for count in range(0, max_line):

        in_range = True
        i = 0
        while in_range:
            line_a = count - i
            line_b = count + i + 1
            #print(line_a, line_b)
            if 0 <= line_a and line_b <= max_line:
                if pattern[line_a] == pattern[line_b]:
                    #print(pattern[line_a], line_a, 0)
                    #print(pattern[line_b], line_b, max_line)

                    if line_a == 0 or line_b == max_line:
                        #print(line_a, line_b, int((line_b + line_a + 1) / 2))
                        return int((line_b + line_a + 1) / 2)
                else:
                    break
                i += 1
            else:
                in_range = False

    return 0


def get_reflections(data):
    sum_pattern_notes = 0
    for pattern in data:
        horizontal = check_mirrors(pattern) * 100
        trans_pattern = list(map(list, zip(*pattern)))
        vertical = check_mirrors(trans_pattern)
        sum_pattern_notes += vertical + horizontal
    return sum_pattern_notes


input_data = get_data()
#print(input_data)
solution1 = get_reflections(input_data)
print(f"Solution 1: {solution1}")

