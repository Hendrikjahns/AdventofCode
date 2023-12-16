import copy

def get_data():
    with open("input_day10.txt") as file:
        data = [list(i) for i in file.read().splitlines()]
    return data


def navigate_pipes(data):
    data2 = copy.deepcopy(data)
    x_start, y_start, x_start2, y_start2 = find_start_point(data)
    print(x_start, y_start, x_start2, y_start2)
    count_path = 1
    direction_dict = {(1, 0): {"7": (0, 1), "J": (0, -1), "-": (1, 0)},
                      (-1, 0): {"F": (0, 1), "L": (0, -1), "-": (-1, 0)},
                      (0, 1): {"J": (-1, 0), "L": (1, 0), "|": (0, 1)},
                      (0, -1): {"7": (-1, 0), "F": (1, 0), "|": (0, -1)},
                      }

    direction = (x_start2 - x_start, y_start2 - y_start)
    x, y = x_start2, y_start2
    data2[y][x] = "P"

    while (x, y) != (x_start, y_start):
        pipe = data[y][x]
        x_new, y_new = x + direction_dict[direction][pipe][0], y + direction_dict[direction][pipe][1]
        direction = (x_new - x, y_new - y)
        x, y = x_new, y_new
        count_path += 1

        data2[y][x] = "P"

    return int(count_path/2), data2


def find_start_point(data):
    for y, line in enumerate(data):
        for x, pipe in enumerate(line):
            if data[y][x] == "S":
                x_start, y_start = x, y
                break

    if data[y_start - 1][x_start] in ("|", "F", "7"):
        x_start2, y_start2 = x_start, y_start - 1
    elif data[y_start + 1][x_start] in ("|", "L", "J"):
        x_start2, y_start2 = x_start, y_start + 1
    elif data[y_start][x_start + 1] in ("-", "J", "7"):
        x_start2, y_start2 = x_start + 1, y_start
    elif data[y_start][x_start - 1] in ("-", "F", "L"):
        x_start2, y_start2 = x_start - 1, y_start

    return x_start, y_start, x_start2, y_start2


def find_enclosed_tiles(data2):
    for line in data2:
        print(line)
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    max_x, max_y = len(data2[0]) - 1, len(data2) - 1
    tiles_queue = []
    sum_enclosed = 0
    for y, line in enumerate(data2):
        for x, pipe in enumerate(line):
            if data2[y][x] not in ("P", "E", "S"):
                tiles_queue.append((x, y))
                data2[y][x] = "E"
                enclosed = 1
                edge = False
                print("new:", enclosed, tiles_queue)
                while len(tiles_queue) > 0:
                    (x_queue, y_queue) = tiles_queue.pop()

                    for dx, dy in neighbors:
                        if x_queue + dx < 0 or x_queue + dx > max_x or y_queue + dy < 0 or y_queue + dy > max_y:
                            edge = True
                            break
                        elif data2[y_queue + dy][x_queue + dx] not in ("P", "E"):
                            tiles_queue.append((x_queue + dx, y_queue + dy))
                            data2[y_queue + dy][x_queue + dx] = "E"
                            enclosed += 1

                if not edge:
                    print("final:", enclosed)
                    sum_enclosed += enclosed
    for line in data2:
        print("".join(line))

    return sum_enclosed



input_data = get_data()
solution1, input_data_2 = navigate_pipes(input_data)
print(f"Solution 1: {solution1}")

solution2 = find_enclosed_tiles(input_data_2)
print(f"Solution 2: {solution2}")

