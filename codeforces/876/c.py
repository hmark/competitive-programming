import sys

input = sys.stdin.readline


def task(n, a):
    if a[n - 1] == 1:
        print("NO")
        return
    else:
        print("YES")

    ans = []
    shift = 0
    for i in reversed(range(1, n)):
        curr = a[i]
        nxt = a[i - 1]
        if curr == 0:
            ans.append(0)
        else:
            shift += 1
            if nxt == 1:
                ans.append(0)
            else:
                ans.append(shift)
                shift = 0

    if a[0] == 0:
        ans.append(0)
    else:
        ans.append(shift + 1)

    print(" ".join([str(x) for x in ans]))


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
