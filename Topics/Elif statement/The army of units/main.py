number_of_units = int(input())

if number_of_units < 1:
    print("no army")
elif number_of_units < 10:
    print("few")
elif number_of_units < 50:
    print("pack")
elif number_of_units < 500:
    print("horde")
elif number_of_units < 1000:
    print("swarm")
elif number_of_units >= 1000:
    print("legion")
