num_1 = float(input())
num_2 = float(input())
operation = input()

result = 0.0

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "pow":
    result = num_1 ** num_2

if operation in ("/", "mod", "div"):
    if num_2 == 0.0:
        result = "Division by 0!"
    else:
        if operation == "/":
            result = num_1 / num_2
        elif operation == "div":
            result = num_1 // num_2
        elif operation == "mod":
            result = num_1 % num_2

print(result)
