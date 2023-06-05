def task(n, s, a):
    mn = 10000000000
    idx = -1
    for i in range(n):
        if a[i] < mn:
            mn = a[i]
            idx = i

    for j in range(idx, n):
        print(s[j])

    for j in range(0, idx):
        print(s[j])


n = int(input())
s = []
a = []
for i in range(n):
    ss, aa = input().split()
    s.append(ss)
    a.append(int(aa))
task(n, s, a)
