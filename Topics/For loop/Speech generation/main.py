phone_number = input()
number_aloud = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for digit in phone_number:
    print(number_aloud[int(digit)])
