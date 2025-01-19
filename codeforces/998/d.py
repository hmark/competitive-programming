import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    for i in range(1, n):
        if a[i-1] > a[i]:
            print("NO")
            return
        mn = min(a[i-1], a[i])
        a[i-1] -= mn
        a[i] -= mn
    
    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
