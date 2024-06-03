import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a, b, m, d):
    bset = set(b)
    cache = {}
    # print(a, b, d)

    if d[-1] in bset:
        for i in range(n):
            if a[i] != b[i]:
                if b[i] in cache:
                    cache[b[i]] += 1
                else:
                    cache[b[i]] = 1

        for dd in d:
            if dd in cache and cache[dd] > 0:
                cache[dd] -= 1

        for x in cache:
            if cache[x] != 0:
                print("NO")
                return

        print("YES")
        return
    else:
        print("NO")
        return


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    task(n, a, b, m, d)
