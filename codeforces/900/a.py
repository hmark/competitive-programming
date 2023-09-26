import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    for x in a:
        if x == k:
            print("YES")
            return
    print("NO")


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
