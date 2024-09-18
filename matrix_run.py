def min_penalty(rows, cols, mtr):
    dp = [[0] * m for _ in range(n)]
    for j in range(m):
        dp[0][j] = matrix[0][j] 
    for i in range(1, n):
        for j in range(m):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            if j < m - 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
            dp[i][j] += matrix[i][j]
    return min(dp[n - 1])


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    matrix = [list(map(int, file.readline().split())) for _ in range(n)]
min_penalty_value = min_penalty(n, m, matrix)
with open('output.txt', 'w') as file:
    file.write(str(min_penalty_value))