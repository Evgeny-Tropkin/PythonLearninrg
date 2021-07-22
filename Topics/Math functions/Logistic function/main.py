import math

x = int(input())

res = 1 / (1 + math.exp(-x))
print(round(res, 2))
