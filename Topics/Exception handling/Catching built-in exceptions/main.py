def exception_check(a, b):
    try:
        res = a / b

    except ZeroDivisionError:
        print("The Error!")

    else:
        print(res)
