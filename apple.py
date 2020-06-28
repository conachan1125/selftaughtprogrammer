class Apple:
    def __init__(self, w, c, p, pr):
        self.weight = w
        self.color = c
        self.place = p
        self.price = pr
        print("created")

ap1 = Apple(100, "dark red", "青森", 150)
print(ap1.price)
