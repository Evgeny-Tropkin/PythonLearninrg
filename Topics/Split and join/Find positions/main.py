number_sequence = [int(num_string) for num_string in input().split()]
searched_number = int(input())
positions = []

for item_num, value in enumerate(number_sequence):
    if value == searched_number:
        positions.append(str(item_num))

if len(positions) > 0:
    print(' '.join(positions))
else:
    print("not found")
