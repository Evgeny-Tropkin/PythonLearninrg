# the list "walks" is already defined
sum_of_distances = 0
for walk in walks:
    sum_of_distances += walk["distance"]

print(int(sum_of_distances / len(walks)))
