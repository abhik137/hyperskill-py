class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 0.5 * leg_1 * leg_2

    def is_right_triangle(self):
        lhs = self.c ** 2
        rhs = self.a ** 2 + self.b ** 2
        if lhs == rhs:
            return True
        return False


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
tr = RightTriangle(input_c, input_a, input_b)

if tr.is_right_triangle():
    area = tr.area
    print(f'{area:.1f}')
else:
    print("Not right")
