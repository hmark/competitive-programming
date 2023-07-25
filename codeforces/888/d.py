import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    st = set()
    for i in range(1, n + 1):
        st.add(i)

    s = []
    s.append(a[0])

    for i in range(1, n - 1):
        s.append(a[i] - a[i-1])

    # print(st)
    prob = None
    for x in s:
        if x in st:
            st.remove(x)
        else:
            prob = x

    # print(s, st, prob)
    st = list(st)

    if len(st) == 2 and st[0] + st[1] == prob:
        print("YES")
    elif len(st) == 1 and prob == None:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
