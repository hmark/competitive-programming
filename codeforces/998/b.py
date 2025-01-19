import sys
import math
from collections import deque
from functools import cmp_to_key

input = sys.stdin.readline

def compare(a, b):
    i = 1
    while i < len(a):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
        i += 1
    return -1

def task(n, m, a):
    a = sorted(a, key=cmp_to_key(compare))

    # print(a)
    mn = -1
    for i in range(1, m + 1):
        for j in range(n):
            if a[j][i] <= mn:
                print(-1)
                return
            else:
                mn = a[j][i]

    ans = []
    for aa in a:
        ans.append(str(aa[0]))
    print(" ".join(ans))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([i+1] + sorted(list(map(int, input().split()))))
    task(n, m, a)
