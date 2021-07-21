def check():
    try:
        num = int(input())
        if 25 <= num <= 37:
            print(num)
        else:
            print("Correct the error!")
    except ValueError:
        print("Correct the error!")
