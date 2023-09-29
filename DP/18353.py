# 병사 배치하기
# https://www.acmicpc.net/problem/18353

n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(len(lst) - max(dp))
