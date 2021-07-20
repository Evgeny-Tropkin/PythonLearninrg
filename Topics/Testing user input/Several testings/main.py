def check(q):
    if not q.isdigit():
        print("It is not a number!")
    else:
        if int(q) >= 202:
            print(q)
        else:
            print("There are less than 202 apples! You cheated on me!")
