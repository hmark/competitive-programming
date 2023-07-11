import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    if n >= 3:
        ans = [str(i) for i in range(4, n + 1)]
        j = max(0, (n - 3) // 2)
        ans = ['2'] + ans[0:j] + ['1'] + ans[j:] + ['3']
        print(' '.join(ans))
    elif n == 2:
        print('2 1')
    else:
        print('1')


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
