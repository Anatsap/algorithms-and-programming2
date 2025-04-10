from collections import deque
import os


def bfs(n, start_x, start_y, final_x, final_y):
    visited = set()
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]
    queue = deque()
    queue.append((start_x, start_y, 0, [(start_x, start_y)]))

    while queue:
        current_x, current_y, level, path = queue.popleft()
        if (current_x, current_y) == (final_x, final_y):
            print("Шлях коня:", path)
            return level
        if (current_x, current_y) in visited:
            continue

        visited.add((current_x, current_y))

        for k in range(n):
            new_x = current_x + row[k]
            new_y = current_y + col[k]
            if 0 <= new_x < n and 0 <= new_y < n:
                new_path = path + [(new_x, new_y)]
                queue.append((new_x, new_y, level + 1, new_path))

    return -1
# print(bfs(8, 7, 0, 0, 7))
file_path = "input.txt"
if os.stat(file_path).st_size == 0:
    print("File is empty, you can not move a knight")
else:
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
        start_x, start_y = map(int, file.readline().strip().split(","))
        final_x, final_y = map(int, file.readline().strip().split(","))
        for line in file:
            coordinates = line.strip().split(",")
            for coordinate in coordinates:
                if coordinate == "None":
                    continue

        print(
            "Minimum number of moves for a knight: ",
            bfs(n, start_x, start_y, final_x, final_y),
        )