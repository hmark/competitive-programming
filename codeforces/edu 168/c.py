import sys
import math
from collections import deque

def task(n, s):
    queue = deque()
    ans = 0
    for i in range(n):
        c = s[i]
        if c == "(" or (c == "_" and len(queue) == 0):
            queue.append(i)
        else:
            value = queue.pop()
            ans += i - value

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
