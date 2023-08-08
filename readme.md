# Python Tips

### Sort 2 related arrays A,B

```python
ab = [[x, y] for x, y in zip(a, b)]
ab.sort()
```

### Fast IO input

```python
import sys
input = sys.stdin.readline
```

### Sort 2D array by xth element

```python
a = [[5,3],[4,7]]
a.sort(key=lambda x: x[1])
```

### Sort 2D array by multiple elements

```python
a = [[5,3],[4,7]]
a.sort(key=lambda x: (x[1], -x[0]), reverse=True)
```
