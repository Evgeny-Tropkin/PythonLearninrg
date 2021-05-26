numbers = []
while True:
    num = input()
    if num == ".":
        break
    numbers.append(int(num))

print(sum(numbers) / len(numbers))
