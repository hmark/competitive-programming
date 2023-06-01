from collections import deque


def task(n, uvs):
    cache = {}
    unvisited = set()

    for i in range(n):
        unvisited.add(i + 1)

    for i in range(n - 1):
        u = uvs[i][0]
        v = uvs[i][1]

        if not u in cache:
            cache[u] = {}

        if not v in cache:
            cache[v] = {}

        cache[u][v] = i + 1
        cache[v][u] = i + 1

    q_next = deque()
    q_next.append([1, 0])
    unvisited.remove(1)
    ans = 0

    while len(unvisited) > 0:
        ans += 1
        q = q_next
        q_next = deque()

        while len(unvisited) > 0 and len(q) > 0:
            u, idx = q.popleft()

            if u in cache:
                to_remove = []
                for v in cache[u]:
                    if v in unvisited and cache[u][v] > idx:
                        unvisited.remove(v)
                        q.append([v, cache[u][v]])
                        q_next.append([v, 0])
                        to_remove.append([u, v])

                for u, v in to_remove:
                    del cache[u][v]
                    del cache[v][u]

                    if len(cache[u]) == 0:
                        del cache[u]

                    if len(cache[v]) == 0:
                        del cache[v]

    print(ans)


t = int(input())
for i in range(0, t):
    n = int(input())
    uv = []
    for i in range(n - 1):
        uv.append(list(map(int, input().split())))
    task(n, uv)
