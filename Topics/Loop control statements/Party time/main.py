input_data = []
while True:
    name = input()
    if name == ".":
        break
    input_data.append(name)

print(input_data)
print(len(input_data))
