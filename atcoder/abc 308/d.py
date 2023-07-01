import sys
import math
from collections import deque


def task(h, w, s):
    q = deque()
    pos = (0, 0)
    q.append(pos)
    dirs = {
        's': 'n',
        'n': 'u',
        'u': 'k',
        'k': 'e',
        'e': 's',
    }

    while len(q) > 0:
        x, y = q.popleft()

        if x == w - 1 and y == h - 1:
            print("Yes")
            return

        c = s[y][x]
        s[y][x] = ''

        if not c in dirs:
            continue

        if x > 0 and s[y][x - 1] == dirs[c]:
            q.append([x - 1, y])
        if x < w - 1 and s[y][x + 1] == dirs[c]:
            q.append([x + 1, y])
        if y > 0 and s[y - 1][x] == dirs[c]:
            q.append([x, y - 1])
        if y < h - 1 and s[y + 1][x] == dirs[c]:
            q.append([x, y + 1])

        # print(c, q, s)

    print('No')


h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))
task(h, w, s)
