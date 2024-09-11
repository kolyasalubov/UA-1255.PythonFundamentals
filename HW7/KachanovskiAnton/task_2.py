import math

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius * radius

def main():
    print("""Choose the shape to calculate the area:
1. Rectangle
2. Triangle
3. Circle""")
    
    user_choice = input("Enter the number of your choice: ")

    if user_choice == '1':
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(width, height)}")
    
    elif user_choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(base, height)}")
    
    elif user_choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_circle(radius)}")
    
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
