import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    a.sort(reverse=True)
    ans = 0
    for i in range(0, n, 2):
        if i + 1 < n:
            diff = a[i] - a[i + 1]

            if k > 0:
                if diff <= k:
                    k -= diff
                    diff = 0
                else:
                    diff -= k
                    k = 0

            ans += diff
        else:
            ans += a[i]
    
    print(ans)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
