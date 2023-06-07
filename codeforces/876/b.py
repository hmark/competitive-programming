import sys

input = sys.stdin.readline


def task(n, ab):
    for i in range(1, n + 1):
        ab[i].sort(reverse=True)

    ans = 0
    on = 0
    ons = {}
    limit = 0

    for a in range(1, n + 1):
        for b in ab[a]:
            if a <= limit:
                break

            ans += b
            on += 1

            if not a in ons:
                ons[a] = 0
            ons[a] += 1

            if on in ons:
                limit = on
                temp = on
                on -= ons[on]
                del ons[temp]

    print(ans)


t = int(input())
for i in range(0, t):
    n = int(input())
    ab = [[] for i in range(n + 1)]
    for j in range(n):
        a, b = map(int, input().split())
        ab[a].append(b)

    task(n, ab)
