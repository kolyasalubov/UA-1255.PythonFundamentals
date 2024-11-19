# Task 1
class Polygon():
    def __init__(self, quantity_of_sides):
        self.quantity_of_sides = quantity_of_sides
    #     self.sides = [0 for i in range(quantity_of_sides)]
    #
    # def set_sides(self, *sides):
    #     if len(sides) == self.quantity_of_sides:
    #         self.sides = sides
    #     else:
    #         return f"Expected {self.quantity_of_sides} sides, get {len(sides)}"
    #
    # def get_sides(self):
    #     return self.sides

class Rectangle(Polygon):
    def __init__(self, height, width):
        # Polygon.__init__(self)
        super().__init__(quantity_of_sides = 2)
        self.height = height
        self.width = width

    def get_square(self):
        return self.height * self.width

rectangle1 = Rectangle(10,12)
print(rectangle1.get_square())

# Task 2
class Human():

    def __init__(self, name):
        self.name = name
    species = "Homosapiens"

    def say_hi(self):
        print(f"Hello {self.name}. How are you?")

    @classmethod
    def get_species(cls):
        print(f"Every human is {cls.species}")

    @staticmethod
    def static_message():
        print(f"Every human is {Human.species} but not every {Human.species} is human")

human1 = Human("John")
human1.say_hi()

# Task 3

class Employee():
    """
    This clas hold information about employees, namely name and salary
    """
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def get_employee_quantity(cls):
        print(f"Quantity of all employees is {cls.count}")

    def get_info(self):
        print(f"Name - {self.name} \nSalary - {self.salary}")

employee1 = Employee("Mike", 3000)
employee1.get_employee_quantity()
employee1.get_info()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
