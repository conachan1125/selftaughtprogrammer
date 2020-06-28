class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_permiter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_permiter(self):
        return self.s1 * 4

    def change_size(self, c1):
        self.s1 += c1

re1 = Rectangle(10, 20)
print(re1.calculate_permiter())
re1.what_am_i()

sq1 = Square(10)
print(sq1.calculate_permiter())

sq1.change_size(5)
print(sq1.calculate_permiter())
sq1.what_am_i()
