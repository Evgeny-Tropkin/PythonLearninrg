def multiply(a, b):

    if b == 1:
        return a

    return a + multiply(a, b - 1)
