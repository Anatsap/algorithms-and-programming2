from collections import deque
import os


def bfs(n, start_x, start_y, final_x, final_y):
    visited = set()
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]
    level = 0
    queue = deque([(start_x, start_y, level)])
    while queue:
        current_x, current_y, level = queue.popleft()
        if [current_x, current_y] == [final_x, final_y]:
            return level
        for k in range(8):
            new_x = current_x + row[k]
            new_y = current_y + col[k]
            if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, level + 1))

    return -1


print(bfs(8, 7, 0, 0, 7))
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
