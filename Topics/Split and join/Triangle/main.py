height = int(input())
width = (height * 2) - 1

for i in range(1, height * 2, 2):
    s = '#' * i
    print(s.center(width))
