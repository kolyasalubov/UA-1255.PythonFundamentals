class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def display_sides(self):
        return f"Цей багатокутник має {self.sides} сторін."

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)  # Прямокутник завжди має 4 сторони
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
print(f"Площа прямокутника: {rectangle.area()}")
