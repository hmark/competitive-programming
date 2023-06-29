import sys
import math
from collections import deque

input = sys.stdin.readline


def task(xa, ya, xb, yb, xc, yc):
    ans = 1
    if xb > xa and xc > xa:
        ans += min(xb, xc) - xa
    elif xa > xb and xa > xc:
        ans += xa - max(xb, xc)

    if yb > ya and yc > ya:
        ans += min(yb, yc) - ya
    elif ya > yb and ya > yc:
        ans += ya - max(yb, yc)

    print(ans)


t = int(input())
for _ in range(t):
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())
    task(xa, ya, xb, yb, xc, yc)
