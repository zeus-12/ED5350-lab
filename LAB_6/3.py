class Polygon:
    def __init__(self, length):
        self.length = length

class Square(Polygon):
    def __init__(self, length):
        super().__init__(length)
        
    def findarea(self):
        return self.length**2

sqr = Square(12)
print(sqr.findarea())



