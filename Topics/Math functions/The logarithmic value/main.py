import math

num = int(input())
base = int(input())
res = 0.0

if base < 2:
    res = math.log(num)
else:
    res = math.log(num, base)

print(round(res, 2))