def task(n, k):
    ans = 0
    spaces = 0
    for i in range(n):
        if i == n - 1:
            ans += 1
        elif spaces == 0:
            ans += 1
            spaces = k - 1
        else:
            spaces -= 1

    print(ans)


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    task(n, k)
