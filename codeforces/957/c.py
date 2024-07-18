import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, k):
    ans = []
    
    for i in reversed(range(m + 1, n + 1)):
        ans.append(str(i))
    
    for i in range(1, m + 1):
        ans.append(str(i))

    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    task(n, m, k)
