# 1240
# https://www.acmicpc.net/problem/1240

import queue

n, m = map(int, input().split())
tree = []
qst = []

for _ in range(n-1):
    dist = list(input())
    tree.append(dist)

for _ in range(m):
    nodes = list(input())
    qst.append(nodes)

def bfs(start, find):
    queue = dequ

