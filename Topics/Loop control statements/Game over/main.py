scores = input().split()
correct = 0
incorrect = 0

for answer in scores:
    if answer == "C":
        correct += 1
    if answer == "I":
        incorrect += 1
    if incorrect > 2:
        print("Game over")
        break
else:
    print("You won")

print(correct)
