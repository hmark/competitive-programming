import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, uv):
    g = {}
    for i in range(1, n + 1):
        g[i] = []

    for i in range(n - 1):
        u, v = uv[i]
        g[u].append(v)
        g[v].append(u)

    leafs = set()
    for i in range(1, n + 1):
        if len(g[i]) == 1:
            leafs.add(i)

    stars = set()

    while len(leafs) > 0:
        leaf = leafs.pop()
        star = g[leaf][0]
        if not star in stars:
            stars.add(star)

            for starleaf in g[star]:
                if len(g[starleaf]) > 1:
                    for starleafleaf in g[starleaf]:
                        if starleafleaf != star:
                            g[starleafleaf].remove(starleaf)
                            leafs.add(starleafleaf)
                    g[starleaf] = [star]

    stars = [len(g[x]) for x in stars]
    stars.sort()

    print(" ".join([str(star) for star in stars]))


n = int(input())
uv = []
for _ in range(n):
    uv.append(list(map(int, input().split())))
task(n, uv)
