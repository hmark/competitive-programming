import sys
import math
from collections import deque

n, m = map(int, input().split())

visited = set()
visited.add(1)
path = deque()
path.append(1)


def task(vs):
    # print(vs)
    for v in vs:
        if not v in visited:
            visited.add(v)
            path.append(v)
            print(v)
            return v == n

    path.pop()
    print(path[-1])
    return False


while True:
    s = input()
    if s == "OK" or s == "-1":
        break
    kv = list(map(int, s.split()))
    k = kv[0]
    vs = kv[1:]
    if task(vs):
        break
