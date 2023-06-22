import sys
import math
from collections import deque


def task(h, w, a):
    for i in range(h):
        for j in range(w):
            n = 0
            if a[i][j] != '.':
                continue
            if i < h - 1 and a[i + 1][j] == '#':
                n += 1
            if i > 0 and a[i - 1][j] == '#':
                n += 1
            if j < w - 1 and a[i][j + 1] == '#':
                n += 1
            if j > 0 and a[i][j - 1] == '#':
                n += 1
            if n >= 2:
                print(i + 1, j + 1)
                return


h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(input()))

task(h, w, a)
