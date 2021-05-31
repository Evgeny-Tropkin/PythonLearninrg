inp_string = input()
numbers = [int(n) for n in inp_string]
result = []

for i in range(len(numbers) - 1):
    result.append((numbers[i] + numbers[i + 1]) / 2)

print(result)
