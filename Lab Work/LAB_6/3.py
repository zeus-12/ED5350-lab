class Polygon:
    def __init__(self, length):
        self.length = length

class Square(Polygon):
    def findarea(self):
        super().__init__(self.length)
        return self.length**2

sqr = Square(12)
print(sqr.findarea())



