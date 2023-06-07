import sys

input = sys.stdin.readline


def task(n, a):
    mn = min(a)
    mx = max(a)
    if mn < 0:
        print(mn)
    else:
        print(mx)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
