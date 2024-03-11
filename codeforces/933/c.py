import sys
import math
from collections import deque


def task(n, s):
    ans = 0
    i = 0
    while i < n:
        s5 = s[i:i+5]
        s3 = s[i:i+3]
        if s5 == "mapie":
            ans += 1
            i += 5
        elif s3 == "map" or s3 == "pie":
            ans += 1
            i += 3
        else:
            i += 1

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
