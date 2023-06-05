import math


def task(n, d, x, y):
    healthy = set()
    for i in range(n):
        healthy.add(i)

    sick = set()

    ans = ["No"] * n
    sick.add(0)
    healthy.remove(0)
    ans[0] = "Yes"

    while len(sick) > 0:
        i = sick.pop()
        infected = []

        for j in healthy:
            distance = math.sqrt(
                math.pow(x[i] - x[j], 2) + math.pow(y[i] - y[j], 2)
            )

            if distance <= d:
                infected.append(j)
                sick.add(j)

        for inf in infected:
            healthy.remove(inf)
            ans[inf] = "Yes"

    for s in ans:
        print(s)


n, d = map(int, input().split())
x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
task(n, d, x, y)
