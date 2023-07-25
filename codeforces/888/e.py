import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, c, p, m):
    g = {}
    dg = {}
    q = deque()
    dp = [None] * (n + 1)

    for pp in p:
        q.append(pp)
        dp[pp] = 0

    for i in range(n):
        u = i + 1

        if not u in g:
            g[u] = []
            dg[u] = set()

        if len(m[i]) > 0:
            for v in m[i]:
                if not v in g:
                    g[v] = []
                    dg[v] = set()

                if dp[u] == None:
                    dg[u].add(v)

                g[u].append(v)
                g[v].append(u)

    for i in range(n):
        u = i + 1
        if len(dg[u]) == 0 and dp[u] == None:
            q.append(u)
            dp[u] = c[u - 1]
    # print("---")
    while len(q) > 0:
        # print(g)
        # print(dg)
        # print(q, dp)
        u = q.popleft()
        for v in g[u]:
            if u in dg[v]:
                dg[v].remove(u)
                if dp[v] == None:
                    dp[v] = 0
                dp[v] += dp[u]
                if len(dg[v]) == 0:
                    q.append(v)
                    dp[v] = min(dp[v], c[v - 1])

    ans = [str(x) for x in dp[1:]]
    print(" ".join(ans))
    # print(dp)
    # print(g)
    # print(dg)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    m = []
    for i in range(n):
        mm = list(map(int, input().split()))
        m.append(mm[1:])
    task(n, k, c, p, m)
