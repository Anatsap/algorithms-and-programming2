import os
import time

from itertools import combinations


def brute_force_greedy_set_cover(employers, sets, n_max):
    uncovered = set(employers)
    solution = []
    best_cover = set()
    breakout = False
    n_evaluations = 0
    n = len(sets)

    for i in range(1, n + 1):
        for subset in combinations(sets, i):
            n_evaluations += 1
            if n_evaluations >= n_max:
                breakout = True
                break
            cover = set.union(*subset)

            if cover == employers:
                return len(subset)
            if len(cover) > len(best_cover):
                best_cover = cover
                solution = list(subset)

        if breakout:
            break

    uncovered -= best_cover
    for v in solution:
        sets.remove(v)

    while uncovered:
        best_set = max(sets, key=lambda s: len(s & uncovered))
        solution.append(best_set)
        uncovered -= best_set
        sets.remove(best_set)
    return len(solution)


def parse_input(line0, line1):
    n, b = list(map(int, line0.strip().split()))
    sorts = [set() for _ in range(b)]
    favourites = list(line1.replace(" ", "").strip())
    for i in range(n):

        for j in range(b):
            index = i * b + j
            if favourites[index] == "Y":
                sorts[j].add(i)

    return set(range(n)), sorts


if __name__ == "__main__":
    file_path = "input.txt"
    if os.stat(file_path).st_size == 0:
        print("File is empty, you can not search sorts of beer")
    else:
        with open(file_path, "r") as file:
            employers, sorts = parse_input(file.readline(), file.readline())
            t0 = time.perf_counter()
            result = brute_force_greedy_set_cover(employers, sorts, 10000000)
            t1 = time.perf_counter()
            print(t1 - t0)
            print(result)