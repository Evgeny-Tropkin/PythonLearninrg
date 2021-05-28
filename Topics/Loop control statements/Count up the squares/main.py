sum_of_numbers = 0
sum_of_squares = 0

while True:
    num = int(input())
    sum_of_numbers += num
    sum_of_squares += num * num
    if sum_of_numbers == 0:
        break

print(sum_of_squares)
