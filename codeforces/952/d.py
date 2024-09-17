import sys
import math
from collections import deque

input = sys.stdin.readline


def task(x, y, z, k):
    x, y, z = map(int, sorted([x,y,z]))

    temp = []
    for i in range(1, 2001):
        if k % i == 0:
            temp.append([k // i, i])

    # print(temp)
    sts = set()
    ans = 0
    for i in range(1, 2001):
        for j in range(len(temp)):
            if temp[j][0] % i == 0:
                xx = temp[j][1]
                yy = i
                zz = temp[j][0] // i

                arr = sorted([xx, yy, zz])
                if arr[0] <= x and arr[1] <= y and arr[2] <= z:
                    st = ",".join(map(str, arr))
                    if not st in sts:
                        sts.add(st)
                        ans = max(ans, (x - arr[0] + 1) * (y - arr[1] + 1) * (z - arr[2] + 1))
    # print(sts)
    print(ans)


t = int(input())
for _ in range(t):
    x, y, z, k = map(int, input().split())
    task(x, y, z, k)
