import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, l, r):
    lbin = -1
    rbin = 1000000000

    while rbin - lbin > 1:
        k = lbin + math.ceil((rbin - lbin) / 2)
        # print(lbin, rbin, k)
        lcurr = 0
        rcurr = 0
        acceptable = True

        for i in range(n):
            ll = l[i]
            rr = r[i]

            lcurr = lcurr - k
            rcurr = rcurr + k

            # print(k, lcurr, rcurr)

            if lcurr > rr or rcurr < ll:
                lbin = k
                acceptable = False
                break

            lcurr = max(lcurr, ll)
            rcurr = min(rcurr, rr)

        if acceptable:
            rbin = k

    print(rbin)


t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    r = []
    for i in range(n):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    task(n, l, r)
