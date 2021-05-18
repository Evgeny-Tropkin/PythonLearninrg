string_of_digits = input()

odd_digits = [int(digit) for digit in string_of_digits if int(digit) % 2 != 0]
print(odd_digits)
