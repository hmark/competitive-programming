import sys
import math
from collections import deque


def task(n, s):
    ans = 0
    i = 0

    if s[i] == '@':
        ans += 1

    while i + 1 < n:
        if s[i + 1] == '@':
            ans += 1
            i = i + 1
        elif i + 2 < n and s[i + 2] == '@':
            ans += 1
            i = i + 2
        elif s[i + 1] == '.':
            i = i + 1
        elif i + 2 < n and s[i + 2] == '.':
            i = i + 2
        else:
            break
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
