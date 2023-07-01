import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, c, d, p):
    cache = {}
    for i in range(m):
        sushi = d[i]
        cache[sushi] = p[i + 1]

    ans = 0
    for i in range(n):
        sushi = c[i]
        if sushi in cache:
            ans += cache[sushi]
        else:
            ans += p[0]
    print(ans)


n, m = map(int, input().split())
c = list(map(str, input().split()))
d = list(map(str, input().split()))
p = list(map(int, input().split()))
task(n, m, c, d, p)
