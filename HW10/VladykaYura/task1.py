class Polygon():
    def __init__(self,sides):
        self.sides = sides
class Rectangle(Polygon):
    def __init__(self,width,height):
        super().__init__(4)
        self.width = width
        self.height = height
    def area (self):
        area = self.width*self.height
        return (area)
square_rectangle = Rectangle(5,10)
print(square_rectangle.area())