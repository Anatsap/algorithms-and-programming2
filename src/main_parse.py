from math import sqrt
import os, time

def wire_length(w, heights):
    n = len(heights)
    max_height = max(heights)
    dp = [[float('-inf')] * (max_height + 1) for _ in range(n)]
    for h in range(1, heights[0] + 1):
        dp[0][h] = 0
    for i in range(1, n):
        for h_i in range(1, heights[i] + 1):
            for h_past in range (1, heights[i-1] + 1):
                dp[i][h_i] = max(dp[i][h_i], dp[i - 1][h_past] + sqrt(w ** 2 + (h_i - h_past) ** 2))

    return max(dp[n - 1])

def parse_input(line0, line1):
    length = int(line0.strip())
    n = list(map(int, line1.strip().split()))
    return length, n

if __name__ == "__main__":
    file_path = "input.txt"
    if os.stat(file_path).st_size == 0:
        print("File is empty, you can not search length of wire")
    else:
        with open(file_path, "r") as file:
            w, heights = parse_input(file.readline(), file.readline())
            t0 = time.perf_counter()
            result = wire_length(w, heights)
            t1 = time.perf_counter()
            print(t1 - t0)
            print(f"{result:.2f}")
