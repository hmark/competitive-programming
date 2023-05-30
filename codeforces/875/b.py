def task(n, a, b):
    cache_a = {}
    last = None
    cntr = 0

    for c in a:
        if last != c:
            cntr = 0

        cntr += 1

        if not c in cache_a:
            cache_a[c] = 0
        cache_a[c] = max(cache_a[c], cntr)

        last = c

    cache_b = {}
    last = None
    cntr = 0
    for c in b:
        if last != c:
            cntr = 0

        cntr += 1

        if not c in cache_b:
            cache_b[c] = 0
        cache_b[c] = max(cache_b[c], cntr)

        last = c

    ans = 0
    for key in cache_a:
        curr = cache_a[key] + (cache_b[key] if key in cache_b else 0)
        ans = max(ans, curr)

    for key in cache_b:
        curr = cache_b[key] + (cache_a[key] if key in cache_a else 0)
        ans = max(ans, curr)

    print(ans)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, a, b)
