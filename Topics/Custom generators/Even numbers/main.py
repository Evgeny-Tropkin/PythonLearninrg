n = int(input())


def even():
    i = 0
    while True:
        yield i
        i += 2


# Don't forget to print out the first n numbers one by one here
g = even()
for num in range(n):
    print(str(next(g)))
