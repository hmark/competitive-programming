import sys
import math
from collections import deque


def task(n, ss):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            s = ss[i] + ss[j]
            if s == s[::-1]:
                print('Yes')
                return
    print('No')


n = int(input())
ss = []
for i in range(n):
    ss.append(input())
task(n, ss)
