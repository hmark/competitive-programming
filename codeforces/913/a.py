import sys
import math
from collections import deque


def task(s):
    col = s[0]
    row = s[1]

    rows = "12345678"
    cols = "abcdefgh"

    for c in cols:
        if col != c:
            print(c + row)

    for c in rows:
        if row != c:
            print(col + c)


t = int(input())
for _ in range(t):
    s = input()
    task(s)
