import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, x, y):
    sumx = sum(x) - x[0]
    sumy = sum(y) - y[0]
    ans = 2 * sumx + 2 * sumy + m * 4
    print(ans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        xx,yy = map(int, input().split())
        x.append(xx)
        y.append(yy)
    task(n, m, x, y)
