import sys
import math
from collections import deque

input = sys.stdin.readline

def find_max_index(a):
    mx = -1
    mx_index = -1
    for i in range(len(a)):
        if a[i] > mx:
            mx = a[i]
            mx_index = i
    return mx_index

def task(n, uv):
    g = {}
    table = [0] * n

    for edge in uv:
        u = edge[0] - 1
        v = edge[1] - 1

        table[u] += 1
        table[v] += 1
        
        if not u in g:
            g[u] = []

        if not v in g:
            g[v] = []

        g[u].append(v)
        g[v].append(u)

    ans = 0

    mx_index = find_max_index(table)
    ans += table[mx_index]
    table[mx_index] = 0
    for edge in g[mx_index]:
        table[edge] -= 1

    mx_index = find_max_index(table)
    ans += table[mx_index] - 1

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    uv = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        uv.append([u, v])
    task(n, uv)

