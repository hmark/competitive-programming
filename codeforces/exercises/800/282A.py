import sys
import math
from collections import deque

def task(n, a):
    ans = 0
    for s in a:
        if s[0] == '+' or s[-1] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)


n = int(input())
a = []
for i in range(n):
    a.append(input())
task(n, a)
