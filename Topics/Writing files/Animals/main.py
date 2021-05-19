# read animals.txt
animals_file = open("animals.txt", "r")
animals = animals_file.readlines()
animals_new = list(map(lambda animal: animal.replace("\n", " "), animals))

# and write animals_new.txt
animals_new_file = open("animals_new.txt", "w")
animals_new_file.writelines(animals_new)

animals_file.close()
animals_new_file.close()
