import sys
import math
from collections import deque

input = sys.stdin.readline


def task(x, y):
    # print(x, y)
    ans = int(math.ceil(y / 2))
    empty = 7 * (ans - 1)

    if y % 2 == 1:
        empty += 11
    else:
        empty += 7

    if x > empty:
        x -= empty
        ans += int(math.ceil(x / 15))

    print(ans)


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    task(x, y)

# for i in range(1, 15):
#     for j in range(1, 100):
#         task(i, j)
