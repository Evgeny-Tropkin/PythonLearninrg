# read sums.txt
sums_file = open("sums.txt", "r")

for line in sums_file:
    numbers = line.split(" ")
    print(int(numbers[0]) + int(numbers[1]))

sums_file.close()
