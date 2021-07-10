def tallest_people(**people):
    max_height = max(people.values())
    the_tallest = [key for key, value in people.items() if value == max_height]

    the_tallest.sort()
    for k in the_tallest:
        print(f"{k} : {people[k]}")
