class Polygon():
    def __init__(self, count_of_side) :
        self.count_of_side = count_of_side
        

class Rectangle(Polygon):
    def __init__(self, side_a, side_b):
        super().__init__(count_of_side=2)
        self.side_a = side_a
        self.side_b = side_b

    def search_of_square_rectangle (self):
        return self.side_a * self.side_b
    

rectangle_1 = Rectangle(side_a= 4, side_b = 5)
square_of_rectangle_1 = rectangle_1.search_of_square_rectangle()
print("Square of rectangle: {}".format( square_of_rectangle_1))