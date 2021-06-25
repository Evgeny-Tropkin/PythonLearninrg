def fibonacci(n):
    i = 1
    i1 = 0
    i2 = 1
    if i == 1:
        i += 1
        yield 0
    if i == 2:
        i += 1
        yield 1
    while i <= n:
        t = i2
        i2 = i2 + i1
        i1 = t
        yield i2
        i += 1
