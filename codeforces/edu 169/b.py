import sys
import math
from collections import deque

input = sys.stdin.readline


def task(la, ra, lb, rb):

    if ra < lb or rb < la:
        print(1)
    else:
        ll = max(la, lb)
        rr = min(ra, rb)
        ans = rr - ll

        if la != lb:
            ans += 1
        
        if ra != rb:
            ans += 1
        print(ans)



t = int(input())
for _ in range(t):
    la, ra = map(int, input().split())
    lb, rb = map(int, input().split())
    task(la, ra, lb, rb)
