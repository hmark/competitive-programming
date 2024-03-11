import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, x, d, c):
    s1 = set()
    s2 = set()
    s2.add(x)

    for i in range(m):
        s1 = s2
        s2 = set()

        dd = d[i]
        cc = c[i]

        for xx in s1:
            if cc == '?' or cc == '0':
                next = xx + dd
                if next > n:
                    next -= n
                s2.add(next)
            if cc == '?' or cc == '1':
                next = xx - dd
                if next < 1:
                    next += n
                s2.add(next)

        if len(s2) == n:
            break

    s2 = sorted(s2)
    print(len(s2))
    print(" ".join([str(ss) for ss in s2]))


t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    d = []
    c = []
    for i in range(m):
        dd, cc = input().split()
        d.append(int(dd))
        c.append(cc)
    task(n, m, x, d, c)
