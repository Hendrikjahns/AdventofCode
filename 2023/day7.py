def get_data():
    with open("input_day7.txt") as file:
        data = [[list(i.split(" ")[0]), int(i.split(" ")[1])] for i in file.read().splitlines()]
        card_dict = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}
        for i, line in enumerate(data):
            for j, card in enumerate(line[0]):
                if card in card_dict.keys():
                    data[i][0][j] = card_dict[card]
                data[i][0][j] = int(data[i][0][j])
    return data


def get_total_winnings(data, part):
    total_winnings = 0
    data_hand_strengths = get_hand_strength(data, part)
    data_hand_strengths.sort(key=lambda strength: (strength[2], strength[0][0], strength[0][1], strength[0][2], strength[0][3], strength[0][4]))
    for count, hand in enumerate(data_hand_strengths):
        winnings = (count + 1) * hand[1]
        total_winnings += winnings
    return total_winnings


def get_hand_strength(hands, part):
    strengths = {"5": 7, "14": 6, "23": 5, "113": 4, "122": 3, "1112": 2, "11111": 1}
    for count, hand in enumerate(hands):
        card_dict = {}

        if part == 2:
            hands[count][0] = [card - 10 if card == 11 else card for card in hand[0]]

        for card in range(1, 15):
            if hand[0].count(card) > 0:
                card_dict[card] = str(hand[0].count(card))

        if part == 2 and 1 in hand[0] and hand[0] != [1, 1, 1, 1, 1]:
            max_card_count = max([item[1] for item in card_dict.items() if item[0] != 1])
            highest_max_card = max([key for key in card_dict.keys() if card_dict[key] == max_card_count])
            card_dict[highest_max_card] = str(int(card_dict[highest_max_card]) + int(card_dict[1]))
            del card_dict[1]

        card_list = list(card_dict.values())
        card_list.sort()
        hand_strength = strengths["".join(card_list)]
        hands[count].append(hand_strength)

    return hands


input_data = get_data()
solution1 = get_total_winnings(input_data, 1)
print(f"Solution 1: {solution1}")

input_data = get_data()
solution2 = get_total_winnings(input_data, 2)
print(f"Solution 2: {solution2}")

