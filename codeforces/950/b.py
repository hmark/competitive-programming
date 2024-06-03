import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, f, k, a):
    fav = a[f - 1]
    a.sort(reverse=True)

    # print(a, a[k-1], fav)

    if a[k - 1] > fav:
        print("NO")
    elif a[k - 1] == fav:
        if k == n or a[k] != fav:
            print("YES")
        else:
            print("MAYBE")
    else:
        print("YES")


t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, f, k, a)
