import math


class Point:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def dist(self, point):
        distance = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return distance
