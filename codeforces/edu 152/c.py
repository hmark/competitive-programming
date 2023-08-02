import sys
import math
from collections import deque


def task(n, m, s, lrs):
    lf = [0] * n
    rg = [0] * n
    lf[0] = -1

    for i in range(n):
        if i > 0:
            lf[i] = lf[i - 1]
        if s[i] == '0':
            lf[i] = i

    rg[n - 1] = n
    for i in reversed(range(n)):
        if i + 1 < n:
            rg[i] = rg[i + 1]
        if s[i] == '1':
            rg[i] = i

    st = set()
    for i in range(m):
        l, r = lrs[i]
        ll = rg[l - 1]
        rr = lf[r - 1]
        if ll > rr:
            st.add((-1, -1))
        else:
            st.add((ll, rr))

    print(len(st))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    lrs = []
    for i in range(m):
        lrs.append(list(map(int, input().split())))
    task(n, m, s, lrs)
