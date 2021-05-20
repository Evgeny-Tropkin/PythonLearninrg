float_list = []
while True:
    inp = input()
    if inp == ".":
        break
    float_list.append(float(inp))

print(min(float_list))
