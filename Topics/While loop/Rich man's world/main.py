deposit = int(input())
count_of_years = 0

while deposit <= 700000:
    deposit *= 1.071
    count_of_years += 1

print(count_of_years)
