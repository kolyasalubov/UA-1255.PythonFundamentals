import math
# Task 1

def higher_number(*args: int) -> int:
    """
    Функція обчислює найбільше число серед заданих.
    Може приймати незліченну кількість аргументів.
    Повертає найбільше число.
    """
    return max(args)

print(higher_number(11, 22))

# Task 2

def rectangle_area(a: int,b: int) -> int:
    return a*b

def triangle_area(a: int,b: int,c: int) -> float:
    p = (a+b+c)/2
    return round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 1)

def circle_area(r: int) -> float:
    PI = 3.14
    return round(PI*r**2, 1)

print(("This program can calculate area of rectangle, triangle and circle"))

while True:
    figure_name = input("Enter name of the figure to calculate area or exit if you want to finish the program - ")
    if figure_name == "rectangle":
        height = int(input("Enter lenght of the first side - "))
        width = int(input("Enter lenght of the second side - "))
        print(f"Area of the renctangle = {rectangle_area(height, width)}")
    elif figure_name == "triangle":
        side_1 = int(input("Enter lenght of the first side - "))
        side_2 = int(input("Enter lenght of the second side - "))
        side_3 = int(input("Enter lenght of the third side - "))
        print(f"Area of the triangle = {triangle_area(side_1, side_2, side_3)}")
    elif figure_name == "circle":
        radius = int(input("Enter radius of the circle - "))
        print(f"Area of the circle = {circle_area(radius)}")
    elif figure_name == "exit":
        break
    else:
        print("Name of the figure is incorrect, please try again")

# Task 3

quantity_of_characters = {}

# for i in "hello":
#     if i in quantity_of_characters:
#         quantity_of_characters[i] += 1
#     else:
#         quantity_of_characters[i] = 1
# print(quantity_of_characters)

def characters_quantity() -> dict:
    for i in "hello":
        if quantity_of_characters.get(i) is None:
            quantity_of_characters[i] = 1
        else:
            quantity_of_characters[i] += 1
    return quantity_of_characters
print(characters_quantity())