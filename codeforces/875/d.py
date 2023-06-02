def task(n, a, b):
    ab = [(x, y) for x, y in zip(a, b)]
    ab.sort()

    ans = 0
    last = 0
    cache = [0] * (2 * n + 1)

    for i in range(n):
        ai = ab[i][0]
        bi = ab[i][1]

        if last != ai:
            if ai * ai > 2 * n + 1:
                break

            last = ai
            cache = [0] * (2 * n + 1)

            for j in range(i + 1, n):
                aj = ab[j][0]
                bj = ab[j][1]
                c = ai * aj - bj

                if c > 0 and c < 2 * n + 1:
                    cache[c] += 1

        ans += cache[bi]

        if i + 1 < n:
            aj = ab[i + 1][0]
            bj = ab[i + 1][1]
            c = ai * aj - bj

            if c > 0 and c < 2 * n + 1:
                cache[c] -= 1

    print(ans)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, a, b)
