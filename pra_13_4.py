class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n

r1 = Rider("cona")
h1 = Horse("conachan", r1)

print(h1.rider.name)
