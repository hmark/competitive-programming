import sys
import math
from collections import deque

input = sys.stdin.readline


def stringify(a, b, c):
    if a == -1:
        aa = "X"
    else:
        aa = a + 1000000

    if b == -1:
        bb = "X"
    else:
        bb = b + 1000000

    if c == -1:
        cc = "X"
    else:
        cc = c + 1000000
    return str(aa) + str(bb) + str(cc)


def task(n, a):
    table = {}
    mem = {}
    ans = 0

    for i in range(n - 2):

        ss = stringify(a[i], a[i+1], a[i+2])

        tests = []
        tests.append(stringify(-1, a[i+1], a[i+2]))
        tests.append(stringify(a[i], -1, a[i+2]))
        tests.append(stringify(a[i], a[i+1], -1))

        for t in tests:
            if t in table:
                ans += table[t]
            if ss in mem:
                ans -= mem[ss]

        s = stringify(-1, a[i+1], a[i+2])
        if not s in table:
            table[s] = 0
        table[s] += 1

        s = stringify(a[i], -1, a[i+2])
        if not s in table:
            table[s] = 0
        table[s] += 1

        s = stringify(a[i], a[i+1], -1)
        if not s in table:
            table[s] = 0
        table[s] += 1

        if not ss in mem:
            mem[ss] = 0
        mem[ss] += 1

    # print(table)
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
