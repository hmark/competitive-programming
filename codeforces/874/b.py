def task(n, k, a, b):
    aa = sorted(a)
    bb = sorted(b)
    table = {}

    for i in range(n):
        if not aa[i] in table:
            table[aa[i]] = []
        table[aa[i]].append(bb[i])

    results = []
    for i in range(n):
        results.append(table[a[i]].pop())
    print(' '.join(map(str, results)))


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, k, a, b)
