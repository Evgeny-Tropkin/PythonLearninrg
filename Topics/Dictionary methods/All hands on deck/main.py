values_of_cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                   "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
sum_of_values = 0

for _ in range(6):
    value_of_card = input()
    sum_of_values += values_of_cards[value_of_card]

print(sum_of_values / 6)
