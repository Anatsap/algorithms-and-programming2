from math import sqrt

def wire_legth(w, heights):
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

if __name__ == "__main__":
    w = int(input())
    heights_b = list(map(int, input().split()))
    result_b = wire_legth(w, heights_b)
    print(f"{result_b:.2f}")



