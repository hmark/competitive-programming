import sys
import math
from collections import deque

input = sys.stdin.readline


def task(q, x):
    ans = []
    first = None
    last = None
    flag = False

    for i in x:
        if not flag:
            if first == None:
                first = i
                last = i
                ans.append('1')
            elif i >= last:
                last = i
                ans.append('1')
            elif i <= first:
                last = -1
                flag = True
            else:
                ans.append('0')

        if flag:
            if last <= i and i <= first:
                last = i
                ans.append('1')
            else:
                ans.append('0')

    print("".join(ans))


t = int(input())
for _ in range(t):
    q = int(input())
    x = list(map(int, input().split()))
    task(q, x)
