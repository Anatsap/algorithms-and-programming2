import os

def greedy_set_cover(employers, sorts):
    uncovered = set(employers)
    n = len(employers)
    b = len(sorts)

    solution = []

    while uncovered:
        best_set = max(sorts, key=lambda s: len(s & uncovered))
        solution.append(best_set)
        uncovered -= best_set
        sorts.remove(best_set)

    return len(solution)

file_path = "input.txt"
if os.stat(file_path).st_size == 0:
    print("File is empty, you can not search sorts of beer")
else:
    with open(file_path, "r") as file:
        n, b = list(map(int, file.readline().strip().split()))
        sorts = [set() for _ in range(b)]

        favourites = list(file.readline().replace(" ", "").strip())
        for i in range(n):
            for j in range(b):
                index = i * b + j
                if favourites[index] == 'Y':
                    sorts[j].add(i)



employers = set(range(n))
result = greedy_set_cover(employers, sorts)
print(result)



