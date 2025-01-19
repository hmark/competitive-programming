import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m1, m2, uvf, uvg):
    g = {}
    g_nodes = set()
    for uv in uvg:
        u = uv[0]
        v = uv[1]
        if not u in g:
            g[u] = {}
        if not v in g:
            g[v] = {}
        g[u][v] = True
        g[v][u] = True
        g_nodes.add(u)
        g_nodes.add(v)

    f = {}
    f_nodes = set()
    for uv in uvf:
        u = uv[0]
        v = uv[1]
        if not u in f:
            f[u] = {}
        if not v in f:
            f[v] = {}
        f[u][v] = True
        f[v][u] = True
        f_nodes.add(u)
        f_nodes.add(v)

    distincts = list((f_nodes ^ g_nodes))
    ans = 0
    adds = 0

    for distinct in distincts:
        if not distinct in g_nodes:
            for edge in f[distinct]:
                del f[edge][distinct]
                ans += 1
            del f[distinct]
        else:
            adds += 1

    has_edge = False
    for edge in f.keys():
        if len(f[edge]) == 0:
            adds += 1
        else:
            has_edge = True

    if adds > 0:
        if has_edge:
            ans += adds
        else:
            ans += adds - 1

    # print(distincts)
    # print(f)
    # print(g)
    print(ans)


t = int(input())
for _ in range(t):
    n, m1, m2 = map(int, input().split())
    uvf = []
    uvg = []
    for i in range(m1):
        uvf.append(sorted(list(map(int, input().split()))))
    for i in range(m2):
        uvg.append(sorted(list(map(int, input().split()))))
    task(n, m1, m2, uvf, uvg)
