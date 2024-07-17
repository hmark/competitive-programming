import sys
import math
from collections import deque

input = sys.stdin.readline


def task(m):
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                ans = abs(i - 2) + abs(j - 2)
                print(ans)
                return


m = []
for i in range(5):
    row = list(map(int, input().split()))
    m.append(row)
task(m)
