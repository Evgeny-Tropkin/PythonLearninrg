n = int(input())


def squares():
    i = 1
    while True:
        yield i * i
        i += 1


# Don't forget to print out the first n numbers one by one here
g = squares()
for num in range(1, n + 1):
    print(str(next(g)))
