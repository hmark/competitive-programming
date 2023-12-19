import sys
import math
from collections import deque


def task(n, s):
    table = []
    for i in range(1, 27):
        table.append(i)

    for c in s:
        table[ord(c) - 65] -= 1

    ans = 0
    for i in range(0, 26):
        if table[i] <= 0:
            ans += 1
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
