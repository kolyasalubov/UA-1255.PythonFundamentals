def Calculates_area_rectangle(a, b):
    print ("Area of Rectangle: ", a * b)

def Calculates_area_triangle(a, h):
     print ("Area of Triangle: ",2*a*h)

def Calculates_area_circle(r):
    PI = 3.14
    print("Area of Circle: ",PI*r**2)

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
    Calculates_area_triangle(r)
