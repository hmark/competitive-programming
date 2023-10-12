import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a, b, c):
    arr = [a, b, c]
    arr.sort()

    if a == b and b == c:
        print("YES")
        return

    for i in range(3):
        mx = arr[-1]
        mn = arr[0]

        arr[-1] = mx - mn
        arr.append(mn)
        arr.sort()

        mx = arr[-1]
        mn = arr[0]

        if mx == mn:
            print("YES")
            return

    print("NO")


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    task(a, b, c)
