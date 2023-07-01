import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            print('No')
            return
        if a[i] < 100 or a[i] > 675:
            print('No')
            return
        if a[i] % 25 != 0:
            print('No')
            return

    print('Yes')


a = list(map(int, input().split()))
task(a)
