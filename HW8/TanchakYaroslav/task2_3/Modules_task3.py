# Task 3 - Calculate the area of figures

import figure_areas

loop_condition = True
while loop_condition:
    chose = input("Enter which area of figure you want to calculate \n1 - rectangle \n2 - triangle \n3 - circle \n4 - Exit \nYour chose is - ")
    if chose == "1":
        height = int(input("Enter height of the rectangle - "))
        width = int(input("Enter width of the rectangle - "))
        print(f"Area of the rectangle is - {figure_areas.rectangle_area(height, width) = }")
    elif chose == "2":
        base = int(input("Enter base of the triangle - "))
        height = int(input("Enter height of the triangle - "))
        print(f"Area of the triangle is - {figure_areas.triangle_area(base, height)}")
    elif chose == "3":
        radius = int(input("Enter radius of the circle - "))
        print(f"Area of the circle is - {figure_areas.circle_area(radius)}")
    elif chose == "4":
        print("See you soon :)")
        loop_condition = False



