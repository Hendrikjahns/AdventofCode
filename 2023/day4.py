def get_data():
    with open("input_day4.txt") as file:
        data = [line.split(": ") for line in file.read().splitlines()]
        for i, line in enumerate(data):
            data[i][1] = data[i][1].split(" | ")
            print(data[i][0])
            data[i][0] = int(data[i][0].replace("Card ", "").strip())
            data[i][1][0] = [i for i in data[i][1][0].replace("  ", " ").split(" ") if i != ""]
            data[i][1][1] = [i for i in data[i][1][1].replace("  ", " ").split(" ") if i != ""]

    return data


def get_winning_numbers(data):
    total_points: int = 0
    card_matches = {}
    for line in data:
        card_number: int = line[0]
        points: int = 0
        matches: int = len(list(set(line[1][0]).intersection(line[1][1])))
        card_matches[card_number] = [matches, 1]
        if matches > 0:
            points = 2 ** (matches - 1)
        total_points += points

    return total_points, card_matches


def get_total_card_number(data, card_matches):
    for card in card_matches.keys():
        for i in range(card + 1, card + card_matches[card][0] + 1):
            card_matches[i][1] += card_matches[card][1]
    return card_matches


input_data = get_data()
solution1, list_card_matches = get_winning_numbers(input_data)
print(f"Solution 1: {solution1}")

list_card_matches = get_total_card_number(input_data, list_card_matches)
solution2 = sum([list_card_matches[key][1] for key in list_card_matches.keys()])
print(f"Solution 2: {solution2}")
