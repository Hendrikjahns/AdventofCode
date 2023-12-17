import copy


def get_data():
    with open("input_day16.txt") as file:
        data = file.read().splitlines()
    return data


def count_energized_tiles(data, starting_point, start_movement):
    movement_dict = {(1, 0): {"\\": (0, 1), "/": (0, -1), "|": [(0, -1), (0, 1)], "-": (1, 0)},
                     (-1, 0): {"\\": (0, -1), "/": (0, 1), "|": [(0, -1), (0, 1)], "-": (-1, 0)},
                     (0, 1): {"\\": (1, 0), "/": (-1, 0), "|": (0, 1), "-": [(1, 0), (-1, 0)]},
                     (0, -1): {"\\": (-1, 0), "/": (1, 0), "|": (0, -1), "-": [(1, 0), (-1, 0)]}
                     }

    open_tiles = [[starting_point, start_movement]]
    print(open_tiles)
    energized_tiles = []
    max_x, max_y = len(data[0]) - 1, len(data) - 1

    while len(open_tiles) > 0:
        current_xy, current_movement = open_tiles.pop()
        energized_tiles.append([current_xy, current_movement])
        next_xy = [current_xy[0] + current_movement[0], current_xy[1] + current_movement[1]]
        if 0 <= next_xy[0] <= max_x and 0 <= next_xy[1] <= max_y:
            next_tile = data[next_xy[1]][next_xy[0]]
            if next_tile == "." or movement_dict[current_movement][next_tile] == current_movement:
                if [next_xy, current_movement] not in energized_tiles:
                    open_tiles.append([next_xy, current_movement])
            elif type(movement_dict[current_movement][next_tile]) is list:
                for split_move in movement_dict[current_movement][next_tile]:
                    if [next_xy, split_move] not in energized_tiles:
                        open_tiles.append([next_xy, split_move])
            else:
                if [next_xy, movement_dict[current_movement][next_tile]] not in energized_tiles:
                    open_tiles.append([next_xy, movement_dict[current_movement][next_tile]])
        else:
            continue

    set_energized_tiles = []
    for tile in energized_tiles:
        if tile[0] not in set_energized_tiles:
            set_energized_tiles.append(tile[0])
    return len(set_energized_tiles) - 1


input_data = get_data()
solution1 = count_energized_tiles(input_data, [-1, 0], (1, 0))
print(f"Solution 1: {solution1}")

energized_tiles_list = []
for i in range(0, len(input_data[0])):
    energized_tiles_list.append(count_energized_tiles(input_data, [i, -1], (0, 1)))
    energized_tiles_list.append(count_energized_tiles(input_data, [i, len(input_data[0])], (0, -1)))
for i in range(0, len(input_data)):
    energized_tiles_list.append(count_energized_tiles(input_data, [-1, i], (1, 0)))
    energized_tiles_list.append(count_energized_tiles(input_data, [len(input_data), i], (-1, 0)))

solution2 = max(energized_tiles_list)
print(f"Solution 2: {solution2}")
