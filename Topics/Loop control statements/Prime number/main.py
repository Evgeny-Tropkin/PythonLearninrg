num = int(input())
is_prime = False

if num > 1:
    for i in range(2, num // 2):
        if num % i == 0:
            break
    else:
        is_prime = True

if is_prime:
    print("This number is prime")
else:
    print("This number is not prime")
