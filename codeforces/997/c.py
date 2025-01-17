import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    ans = []
    ans.append("1")
    for i in range(2):
        for j in range(n // 2):
            ans.append(str(j + 1))
    
    if n % 2 == 0:
        ans = ans[:-1]
    # else:
    #     ans = ans[:-2]

    print(" ".join(ans))



t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
