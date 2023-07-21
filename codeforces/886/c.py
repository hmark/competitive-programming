import sys
import math
from collections import deque


def task(grid):
    ans = []
    for row in grid:
        for c in row:
            if c != '.':
                ans.append(c)

    print("".join(ans))


t = int(input())
for _ in range(t):
    grid = []
    for i in range(8):
        grid.append(list(input()))
    task(grid)
