import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print("作ったよ")

    def area(self):
        return self.radius ** 2 * math.pi

cr1 = Circle(10)
print(cr1.radius)
area = cr1.area()
print(area)
