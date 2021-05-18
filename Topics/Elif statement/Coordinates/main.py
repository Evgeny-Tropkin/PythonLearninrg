coord_x = float(input())
coord_y = float(input())
num_of_quadrant = "It's the origin!"

product = coord_x * coord_y

if product > 0:
    if coord_x > 0:
        num_of_quadrant = "I"
    else:
        num_of_quadrant = "III"
elif product < 0:
    if coord_x < 0:
        num_of_quadrant = "II"
    else:
        num_of_quadrant = "IV"
else:
    if coord_x != 0 or coord_y != 0:
        num_of_quadrant = "One of the coordinates is equal to zero!"

print(num_of_quadrant)
