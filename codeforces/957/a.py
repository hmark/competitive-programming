import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a, b, c):
    ans = a * b * c

    for i in range(0, 6):
        for j in range(0, 6):
            for k in range(0, 6):
                if i + j + k == 5:
                    ans = max(ans, (a + i) * (b + j) * (c + k))
                
    print(ans)


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    task(a, b, c)
