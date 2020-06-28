class Triangle:
    def __init__(self, h, l):
        self.height = h
        self.length = l

    def area(self):
        return self.height * self.length / 2

tr1 = Triangle(10, 50)
print(tr1)
print(tr1.area())
