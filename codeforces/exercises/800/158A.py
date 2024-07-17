import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    ans = 0
    val = a[k - 1]
    for i in range(n):
        if a[i] > 0 and a[i] >= val:
            ans += 1
        else:
            break

    print(ans)



n, k = map(int, input().split())
a = list(map(int, input().split()))
task(n, k, a)
