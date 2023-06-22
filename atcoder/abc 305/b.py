import sys
import math
from collections import deque

input = sys.stdin.readline


def task(p, q):
    dists = [3, 1, 4, 1, 5, 9]
    ans = 0
    mn = min(ord(p), ord(q)) - ord('A')
    mx = max(ord(p), ord(q)) - ord('A')

    for i in range(mn, mx):
        ans += dists[i]

    print(ans)


p, q = map(str, input().split())
task(p, q)
