def task(n, a):
    b = [str(n - x + 1) for x in a]
    print(" ".join(b))


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
