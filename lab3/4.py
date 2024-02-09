from math import sqrt
class Point:
    def show(self):
        print(self.x, self.y, sep = ' ')
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, P2):
        return sqrt((self.x - P2.x) ** 2 + (self.y - P2.y) ** 2)

P1 = Point()
P1.move(0, 0)
P2 = Point()
P2.move(1, 1)
P1.show()
P2.show()

print(P1.dist(P2))