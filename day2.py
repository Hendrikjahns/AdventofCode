def get_data():
    with open("input_day2.txt") as file:
        data = file.read().splitlines()
        data = [i.split(": ") for i in data]
        data = {int(i[0].replace("Game ", "")): i[1].split("; ") for i in data}
        for key in data.keys():
            data[key] = [k.split(", ") for k in data[key]]
            for k, set in enumerate(data[key]):
                data[key][k] = {l.split(" ")[1]: int(l.split(" ")[0]) for l in set}
    return data


def check_games(data, r, g, b):
    id_sum, power_sum = 0, 0
    for game_key in data.keys():
        colors = {"red": [r, 0], "green": [g, 0], "blue": [b, 0]}
        game_possible = True
        for set in data[game_key]:
            for color_key in colors.keys():
                if color_key in set:
                    if set[color_key] > colors[color_key][0]:
                        game_possible = False

                    if colors[color_key][1] < set[color_key]:
                        colors[color_key][1] = set[color_key]

        if game_possible:
            id_sum += game_key

        power_sum += colors["red"][1] * colors["green"][1] * colors["blue"][1]

    return id_sum, power_sum


input_data = get_data()
solution1, solution2 = check_games(input_data, 12, 13, 14)
print(f"Solution 1: {solution1}")
print(f"Solution 2: {solution2}")
