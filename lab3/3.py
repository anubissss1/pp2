class Shape:
    area = 0
    def printArea(self):
        print(self.area)
class Rectangle(Shape):
    def __init__(self, len, wth):
        self.len = len
        self.wth = wth
    def calcArea(self):
        self.area = self.len * self.wth

x = Rectangle(5, 10)
x.calcArea()
x.printArea()