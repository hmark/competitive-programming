import sys
import math
from collections import deque


def task(n, s):
    ans = []
    last = None
    for c in s:
        if last == None:
            ans.append(c)
            last = c
        elif c == last:
            last = None

    print("".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
