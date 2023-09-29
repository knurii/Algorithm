# 숫자고르기
# https://www.acmicpc.net/problem/2668

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
ans = set()

def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            ans.update(first)
            return True
        return False
    return dfs(first, second, arr[num])

for i in range(1, n+1):
    if i not in ans:
        dfs(set(), set(), i)

print(len(ans))
print(*sorted(list(ans)), sep='\n')