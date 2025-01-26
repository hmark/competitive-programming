import sys
import math
from collections import deque


def task(s):
    ans = 0
    for c in s:
        if c == '1':
            ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    s = input()
    task(s)
