def task(w, h, n, p, q, an, a, bn, b):

    a.append(w)
    an += 1

    b.append(h)
    bn += 1

    cache_idx = {}
    for i in range(n):
        cache_idx[str(p[i])+'-'+str(q[i])] = i

    cache_a = {}
    pq = [[x, y] for x, y in zip(p, q)]
    pq.sort()

    a_start = 0
    for i in range(n):
        for j in range(a_start, an):
            a_start = j
            if pq[i][0] < a[j]:
                cache_a[str(pq[i][0])+'-'+str(pq[i][1])] = j
                break

    cache_b = {}
    qp = [[x, y] for x, y in zip(q, p)]
    qp.sort()

    b_start = 0
    for i in range(n):
        for j in range(b_start, bn):
            b_start = j
            if qp[i][0] < b[j]:
                cache_b[str(qp[i][1])+'-'+str(qp[i][0])] = j
                break

    cache = {}
    for key in cache_a:
        part = str(cache_a[key]) + '-' + str(cache_b[key])
        if not part in cache:
            cache[part] = 0
        cache[part] += 1

    if len(cache) < an * bn:
        mn = 0
    else:
        mn = min(cache.values())
    mx = max(cache.values())
    print(mn, mx)


w, h = map(int, input().split())
n = int(input())
p = []
q = []
for i in range(n):
    pp, qq = map(int, input().split())
    p.append(pp)
    q.append(qq)
an = int(input())
a = list(map(int, input().split()))
bn = int(input())
b = list(map(int, input().split()))
task(w, h, n, p, q, an, a, bn, b)
