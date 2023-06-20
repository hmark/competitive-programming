import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, uv, q, xy):
    g = {}

    for i in range(n):
        g[i + 1] = set()

    weights = {}
    for i in range(n):
        weights[i + 1] = 0

    for i in range(n - 1):
        u = uv[i][0]
        v = uv[i][1]
        g[u].add(v)
        g[v].add(u)

    leaves = deque()
    for i in g:
        if i != 1 and len(g[i]) == 1:
            leaves.append(i)
            weights[i] = 1

    while len(g) > 1:
        leaf = leaves.popleft()
        # print(leaf, leaves, g)
        for node in g[leaf]:
            g[node].remove(leaf)
            weights[node] += weights[leaf]
            if len(g[node]) == 1 and node != 1:
                leaves.append(node)
        del g[leaf]
        # print(g)

    # print(weights)
    for i in range(q):
        x = xy[i][0]
        y = xy[i][1]
        print(weights[x] * weights[y])


t = int(input())
for _ in range(t):
    n = int(input())
    uv = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        uv.append([u, v])
    q = int(input())
    xy = []
    for i in range(q):
        x, y = map(int, input().split())
        xy.append([x, y])
    task(n, uv, q, xy)
