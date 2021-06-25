n = int(input())
denominator = int(input())
try:
    print(n // denominator)
except:
    print("Division by zero is not supported")
