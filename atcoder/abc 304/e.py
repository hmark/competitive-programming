def task(n, m, u, v, kn, x, y, qn, p, q):
    cache = {}
    unvisited = set()
    for i in range(n):
        cache[i + 1] = set()
        unvisited.add(i + 1)

    for i in range(m):
        if u[i] != v[i]:
            cache[u[i]].add(v[i])
            cache[v[i]].add(u[i])

    cache_nodes = {}
    g = 0
    while len(unvisited) > 0:
        g += 1
        curr = unvisited.pop()
        queue = cache[curr]
        nodes = {curr}
        cache_nodes[curr] = g

        while len(queue) > 0:
            nxt = queue.pop()
            if nxt in unvisited:
                nodes.add(nxt)
                cache_nodes[nxt] = g
                unvisited.remove(nxt)
                for i in cache[nxt]:
                    queue.add(i)

    cache_conditions = {}
    for i in range(kn):
        condition1 = str(cache_nodes[x[i]]) + '-' + str(cache_nodes[y[i]])
        condition2 = str(cache_nodes[y[i]]) + '-' + str(cache_nodes[x[i]])
        cache_conditions[condition1] = False
        cache_conditions[condition2] = False

    for i in range(qn):
        condition = str(cache_nodes[p[i]]) + '-' + str(cache_nodes[q[i]])
        if condition in cache_conditions:
            print("No")
        else:
            print("Yes")

    # print(cache_nodes)
    # print(cache_conditions)
    # print(n, m, u, v, kn, x, y, qn, p, q)


n, m = map(int, input().split())
u = []
v = []
for i in range(m):
    uu, vv = map(int, input().split())
    u.append(uu)
    v.append(vv)
kn = int(input())
x = []
y = []
for i in range(kn):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
qn = int(input())
p = []
q = []
for i in range(qn):
    pp, qq = map(int, input().split())
    p.append(pp)
    q.append(qq)
task(n, m, u, v, kn, x, y, qn, p, q)
