inp = input()
n = 0
s = 0
while inp != "55":
    n += 1
    s += int(inp)
    inp = input()

print(n)
print(s)

if n > 0:
    print(round(s / n))
