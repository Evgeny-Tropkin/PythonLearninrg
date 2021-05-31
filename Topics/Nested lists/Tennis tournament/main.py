num_of_rows = int(input())
count_of_wins = 0
winners_list = []

for _ in range(num_of_rows):
    message = input()
    if message[-1] == "n":
        count_of_wins += 1
        winners_list.append(message.replace(" win", ''))

print(winners_list)
print(count_of_wins)
