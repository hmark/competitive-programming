import sys

input = sys.stdin.readline


def task(n, m):
    isPrime = True
    for i in range(2, m - 1):
        if m % i == 0:
            isPrime = False

    if not isPrime:
        cnt = 0
        for i in range(n):
            row = []
            for j in range(m):
                cnt += 1
                row.append(str(cnt))
            print(" ".join(row))
    else:
        rows = []
        for i in reversed(range(0, n, 2)):
            rows.append(i)
        for i in reversed(range(1, n, 2)):
            rows.append(i)

        for i in range(n):
            row = []
            for j in range(m):
                row.append(str(rows[i] * m + j + 1))
            print(" ".join(row))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    task(n, m)
