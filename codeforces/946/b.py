import sys
import math
from collections import deque


def task(n, b):
    chars = set()
    for c in b:
        chars.add(c)

    a = sorted(list(chars))
    table = {}

    for i in range(len(a)):
        c = a[i]
        table[c] = a[-i-1]

    ans = []
    for c in b:
        ans.append(table[c])
    print("".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    b = input()
    task(n, b)
