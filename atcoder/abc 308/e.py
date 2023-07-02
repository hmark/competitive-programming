import sys
import math
from collections import deque


def task(n, a, s):
    dpm = []
    dpx = []

    for i in range(n):
        dpm.append([0, 0, 0, 0])
        dpx.append([0, 0, 0, 0])

    for i in range(n):
        if i > 0:
            for j in range(4):
                dpm[i][j] = dpm[i - 1][j]

        if s[i] == 'M':
            x = min(3, a[i])
            dpm[i][x] += 1

    for i in reversed(range(n)):
        if i < n - 1:
            for j in range(4):
                dpx[i][j] = dpx[i + 1][j]

        if s[i] == 'X':
            x = min(3, a[i])
            dpx[i][x] += 1

    ans = 0

    for i in range(n):
        if s[i] == 'E':
            x = min(a[i], 3)

            for j in range(4):
                for k in range(4):
                    st = set()
                    st.add(x)
                    st.add(j)
                    st.add(k)
                    mn = min(st)

                    if mn == 0 and dpm[i][j] > 0 and dpx[i][k] > 0:
                        if not 1 in st:
                            ans += dpm[i][j] * dpx[i][k]
                        elif not 2 in st:
                            ans += 2 * dpm[i][j] * dpx[i][k]
                        elif not 3 in st:
                            ans += 3 * dpm[i][j] * dpx[i][k]
    print(ans)


n = int(input())
a = list(map(int, input().split()))
s = input()
task(n, a, s)
