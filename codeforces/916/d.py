import sys
import math
from collections import deque

input = sys.stdin.readline


def mapper(x):
    return {}


def task(n, a, b, c):
    a = [[i, x] for i, x in enumerate(a)]
    b = [[i, x] for i, x in enumerate(b)]
    c = [[i, x] for i, x in enumerate(c)]

    a = sorted(a, key=lambda x: -x[1])
    b = sorted(b, key=lambda x: -x[1])
    c = sorted(c, key=lambda x: -x[1])

    a = a[0:(min(n, 3))]
    b = b[0:(min(n, 3))]
    c = c[0:(min(n, 3))]

    ans = 0
    for aa in a:
        for bb in b:
            for cc in c:
                if aa[0] != bb[0] and bb[0] != cc[0] and aa[0] != cc[0]:
                    ans = max(ans, aa[1] + bb[1] + cc[1])

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    task(n, a, b, c)
