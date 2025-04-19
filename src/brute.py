import os
from itertools import combinations


def brute_force_set_cover(employers, sets):
    n = len(sets)
    for i in range(1, n + 1):
        for subset in combinations(sets, i):
            if set.union(*subset) == employers:
                return len(subset)


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
                if favourites[index] == "Y":
                    sorts[j].add(i)


employers = set(range(n))
result = brute_force_set_cover(employers, sorts)
print(result)
