class Shape:
    area = 0
    def printArea(self):
        print(self.area)
class Square(Shape):
    def __init__(self, a):
        self.side = a
        self.area = a * a

x = Square(5)
x.printArea()