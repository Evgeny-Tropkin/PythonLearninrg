class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area
        self.area = 0.5 * self.a * self.b

    def is_right(self):
        return self.c * self.c == self.a * self.a + self.b * self.b


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

new_triangle = RightTriangle(input_c, input_a, input_b)
if new_triangle.is_right():
    print(new_triangle.area)
else:
    print("Not right")
