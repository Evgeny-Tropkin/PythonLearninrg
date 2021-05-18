num_sequence = input()

total_sums = [int(digit) for digit in num_sequence]
for i in range(1, len(total_sums)):
    total_sums[i] += total_sums[i - 1]

print(total_sums)
