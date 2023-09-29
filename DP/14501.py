# 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())

dp = [0] * 20
lst = [[0,0]]

for _ in range(n):
    apd_lst = list(map(int, input().split()))
    lst.append(apd_lst)

for i in range(1, n+1):
    x = lst[i][0] - 1
    dp[i] = max(dp[i-1], dp[i])
    dp[i+x] = max(dp[i-1]+lst[i][1], dp[i+x])

print(dp[n])
