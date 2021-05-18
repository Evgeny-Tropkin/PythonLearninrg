input_number = int(input())
result = 0

result += input_number % 10 + (input_number // 10) % 10 + input_number // 100

print(result)
