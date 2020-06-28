class Square:
    square_list = []

    def __init__(self, s):
        self.s = s
        self.square_list.append(s)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s, self.s, self.s, self.s)


def compare(obj1, obj2):
    return obj1 is obj2

     
s1 = Square(10)
s2 = Square(20)
s3 = Square(15)

print(Square.square_list)

print(s1)

print(compare("a", "b"))
