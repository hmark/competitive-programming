import sys

input = sys.stdin.readline


def task(n, p):
    idx_1 = 0
    idx_2 = 0
    idx_n = 0

    for i in range(n):
        if p[i] == 1:
            idx_1 = i
        elif p[i] == 2:
            idx_2 = i
        elif p[i] == n:
            idx_n = i

    if idx_1 < idx_n and idx_n < idx_2:
        print(1, 1)
    elif idx_n < idx_1 and idx_1 < idx_2:
        print(idx_1 + 1, idx_n + 1)
    elif idx_1 < idx_2 and idx_2 < idx_n:
        print(idx_2 + 1, idx_n + 1)
    elif idx_2 < idx_1 and idx_1 < idx_n:
        print(idx_1 + 1, idx_n + 1)
    elif idx_2 < idx_n and idx_n < idx_1:
        print(1, 1)
    elif idx_n < idx_2 and idx_2 < idx_1:
        print(idx_n + 1, idx_2 + 1)


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    task(n, p)
