import math


def calculate_cosine(angle_in_degrees):
    res = round(math.cos(math.radians(angle_in_degrees)), 2)
    print(str(res))