from math import (pow,
                  pi,
                  )
from count_area import (Calculates_area_rectangle,
                        Calculates_area_circle,
                        Calculates_area_triangle)

def main():
    print("1: Area of Rectangle")
    print("2: Area of Triangle")
    print("3: Area of Circle")

    choice = int (input("Your choice (input 1,2 or 3) : "))

    if choice == 1:
        a = int(input("Input width: "))
        b = int(input("Input length: "))
        Calculates_area_rectangle(a,b)
    elif choice == 2:
        a = int(input("Input base: "))
        h = int(input("Input height: "))
        Calculates_area_triangle(a,h)
    elif choice == 3:
        r = int(input("Input radius: "))
        Calculates_area_circle(r)

main()