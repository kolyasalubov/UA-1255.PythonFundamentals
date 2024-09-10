def rectangle_area(width,height):
    area_rectangle = width * height
    return area_rectangle
def triangle_area(base,height):
    area_triangle = (base*height)/2
    return area_triangle
def circle_area (radius):
    area_circle = 3.14*(radius*radius)
    return area_circle

user_choice=0
print("1-Rectangle area\n2-Triangle area\n3-Circle area")
user_choice=int(input("Choise number:"))

while user_choice != 1 and user_choice != 2 and user_choice != 3:
    print("No, enter 1 or 2 or 3")
    print("1-Rectangle area\n2-Triangle area\n3-Circle area")
    user_choice = int(input("Choose number:"))
    

if user_choice == 1:
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))
    print("Rectangle area =",rectangle_area(width,height))
elif user_choice == 2:
    base = float(input("Enter base:"))
    height= float(input("Enter height:"))
    print("Triangle area =",triangle_area(base,height))
elif user_choice == 3:
    radius = float(input("Enter radius:"))
    print("Circle area =",circle_area(radius))