# Task 1
import math

def max_number(num1, num2):
    """
    This function returns the maximum of two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2
    

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = max_number(num1, num2)
print(f"The maximum number is {result}")


# Task 2
def area_rectangle(a, b):
    return a * b

def area_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def area_circle(r):
    return math.pi * r ** 2

while True:
    choice = input("Menu: \n[1] Rectangle \n[2] Triangle \n[3] Circle \n[0] Exit \nChoose a figure: ")
    match choice:
        case "1":
            a = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the width of the rectangle: "))
            result = area_rectangle(a, b)
            print(f"The area of the rectangle is {result}")
        case "2":
            a = float(input("Enter the first side of the triangle: "))
            b = float(input("Enter the second side of the triangle: "))
            c = float(input("Enter the third side of the triangle: "))
            result = area_triangle(a, b, c)
            print(f"The area of the triangle is {result}")
        case "3":
            r = float(input("Enter the radius of the circle: "))
            result = area_circle(r)
            print(f"The area of the circle is {result}")
        case "0":
            print("Goodbye!")
            break
        case _:
            print("Invalid input! Please try again.")


# Task 3

user_input = input("Enter a string: ")
dictionary = {}
for i in user_input:
    dictionary[i] = user_input.count(i)

print(dictionary)