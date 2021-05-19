# create the planets.txt
planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_file = open("planets.txt", "w", encoding="utf-8")

for planet_name in planets_list:
    planets_file.write(planet_name)
    planets_file.write("\n")

planets_file.close()
