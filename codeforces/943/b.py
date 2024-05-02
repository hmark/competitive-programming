import sys
import math
from collections import deque


def task(n, m, a, b):
    start = 0
    ans = 0
    found = False
    for i in range(len(a)):
        found = False
        for j in range(start, len(b)):
            if a[i] == b[j]:
                start = j + 1
                ans += 1
                found = True
                break

        if not found:
            print(ans)
            return
    print(ans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    task(n, m, a, b)
