# 라디오
# https://www.acmicpc.net/problem/3135

a, b = map(int, input().split())
n = int(input())
f_lst = []

for _ in range(n):
    f_lst.append(int(input()))

btn_cnt = 0

m_lst = []
m_lst.append(abs(b-a))

for i in f_lst:
    m_lst.append(abs(b-i))

diff_min = min(m_lst)

if diff_min != m_lst[0]:
    btn_cnt += 1

btn_cnt += diff_min

print(btn_cnt)