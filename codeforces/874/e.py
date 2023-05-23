def task(n, a):
    table = {}
    bag = set()
    for i in range(1, n + 1):
        bag.add(i)

        if not i in table:
            table[i] = set()
        table[i].add(a[i - 1])

        if not a[i - 1] in table:
            table[a[i - 1]] = set()
        table[a[i - 1]].add(i)

    opened = 0
    closed = 0
    while len(bag) > 0:
        curr = bag.pop()
        conns = 2
        nexts = set()

        while True:
            conns = min(conns, len(table[curr]))
            for i in table[curr]:
                if i in bag:
                    nexts.add(i)

            if len(nexts) == 0:
                break

            curr = nexts.pop()
            bag.remove(curr)

        if conns == 2:
            closed += 1
        else:
            opened += 1

    mn = closed
    if opened > 0:
        mn += 1

    mx = closed + opened
    print(mn, mx)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
