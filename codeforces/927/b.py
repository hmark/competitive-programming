import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    ans = 0
    for aa in a:
        if ans % aa == 0:
            ans += aa
        else:
            ans = math.ceil(ans / aa) * aa
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
