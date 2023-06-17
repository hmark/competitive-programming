import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a):
    b = "".join(reversed(a))
    ans = int(b, 2)
    print(ans)


a = list(map(str, input().split()))
task(a)
