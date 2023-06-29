import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, uvy):
    g = {}

    for i in range(m):
        u, v, y = uvy[i]

        if not u in g:
            g[u] = []

        if not v in g:
            g[v] = []

        g[u].append((v, y))
        g[v].append((u, y))

    if not n in g or not 1 in g:
        print('inf')
        return

    visited = set()
    visited.add(1)

    queue = deque()
    queue.append(1)

    ans = []
    total = 0
    s = ["0"] * n
    s[0] = "1"
    nexts = []
    cache = {}
    cache[1] = 0
    last = False

    while not last:
        while len(queue) > 0:
            curr = queue.popleft()

            if curr in g:
                for uv in g[curr]:
                    u, v = uv
                    if not u in visited:
                        nexts.append([u, v + cache[curr]])

                del g[curr]

        nexts.sort(key=lambda x: x[1], reverse=True)

        # print(curr)
        # print(visited)
        # print(g)
        # print(nexts)

        if len(nexts) > 0:
            if nexts[-1][1] > total:
                t = nexts[-1][1] - total
                ans.append(["".join(s), t])
                total += t

            while len(nexts) > 0 and nexts[-1][1] == total:
                u, v = nexts.pop()

                if not u in visited:
                    s[u - 1] = "1"
                    cache[u] = total
                    queue.append(u)
                    visited.add(u)

                    if u == n:
                        last = True
        else:
            print('inf')
            return

    print(total, len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


n, m = map(int, input().split())
uvy = []
for i in range(m):
    uvy.append(list(map(int, input().split())))
task(n, m, uvy)
