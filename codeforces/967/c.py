# Interactive

import sys
import math
from collections import deque

def question(x, y):
    print(f"? {x} {y}")
    sys.stdout.flush()
    res = int(input())
    return res

def task(n):
    unvisited = set([i for i in range(2,n+1)])
    queue = deque([])

    ans = []

    while len(unvisited) > 0:
        if len(queue) > 0:
            aa = queue.popleft()
            start = aa[0]
            end = aa[1]
        else:
            start = 1
            end = min(unvisited)
        
        a = question(start, end)

        if a == start:
            ans.append(str(start))
            ans.append(str(end))
            unvisited.remove(end)
        else:
            if a in unvisited:
                queue.appendleft([start, a])
            queue.appendleft([a, end])

    print(f'! {" ".join(ans)}')


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
