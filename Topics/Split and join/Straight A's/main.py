grades = input().split()

quantity_of_the_best_grade = 0
for grade in grades:
    if grade == 'A':
        quantity_of_the_best_grade += 1

print(round(quantity_of_the_best_grade / len(grades), 2))
