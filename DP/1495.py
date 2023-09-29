# 기타리스트
# https://www.acmicpc.net/problem/1495

n, s, m = map(int, input().split())
vol = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] > 0:
            if 0 <= j+vol[i] <= m:
                dp[i][j+vol[i]] = 1
            if 0 <= j-vol[i] <= m:
                dp[i][j-vol[i]] = 1

ans = -1

for i in range(m+1):
    if dp[n][i] == 1:
        ans = max(ans, i)

print(ans)