    import sys
    import math
    from collections import deque
     
    input = sys.stdin.readline
     
     
    def task(n, x):
        a = [aa for aa in x]
        a.sort()
     
        cache = {}
     
        total = sum(a) - (a[0] - 1) * n
        last = a[0]
        processed = 0
     
        for i in a:
     
            if last != i:
                total -= (i - last) * (n - processed)
                # print(total)
                total += (i - last) * processed
                # print(total)
                last = i
     
            cache[i] = total
            processed += 1
            # print(i, total, processed)
     
        ans = []
        for i in x:
            ans.append(str(cache[i]))
     
        print(" ".join(ans))
     
     
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = list(map(int, input().split()))
        task(n, x)