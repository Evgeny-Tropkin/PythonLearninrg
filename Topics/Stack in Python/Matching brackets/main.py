# put your python code here
stack = []
expression = input()

for item in expression:
    if stack:
        if stack[-1] == '(' and item == ')':
            stack.pop()
            continue
    if item in ['(', ')']:
        stack.append(item)

if stack:
    print("ERROR")
else:
    print("OK")
