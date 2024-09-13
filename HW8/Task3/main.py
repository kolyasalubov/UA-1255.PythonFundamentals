
from Areas_of_figures import rectangle_area,triangle_area,circle_area


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