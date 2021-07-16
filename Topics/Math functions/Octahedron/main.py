import math

edge_length = int(input())

octahedron_area = 2 * math.sqrt(3) * edge_length * edge_length
octahedron_volume = (1 / 3) * math.sqrt(2) * edge_length ** 3

print(round(octahedron_area, 2), round(octahedron_volume, 2))