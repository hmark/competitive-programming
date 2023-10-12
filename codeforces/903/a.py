import sys
import math
from collections import deque


def task(n, m, x, s):
    if x.count(s) > 0:
        print(0)
        return

    x = x + x
    ans = 1

    while True:
        if x.count(s) > 0:
            print(ans)
            return

        if len(x) > len(s) * 2:
            print(-1)
            return

        x = x + x
        ans += 1
        # print('test', x, ans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    task(n, m, x, s)
