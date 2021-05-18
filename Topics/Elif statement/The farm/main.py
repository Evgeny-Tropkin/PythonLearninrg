user_money = int(input())
animal = "None"
cost_per_one_animal = 0
number_of_purchased_animals = ""

if user_money >= 6769:
    animal = "sheep"
    cost_per_one_animal = 6769
elif user_money >= 3848:
    animal = "cow"
    cost_per_one_animal = 3848
elif user_money >= 1296:
    cost_per_one_animal = 1296
    animal = "pig"
elif user_money >= 678:
    animal = "goat"
    cost_per_one_animal = 678
elif user_money >= 23:
    animal = "chicken"
    cost_per_one_animal = 23

if animal != "None":
    number_of_purchased_animals = user_money // cost_per_one_animal
    if number_of_purchased_animals > 1 and animal != "sheep":
        animal += "s"

print(number_of_purchased_animals, animal)
