import math

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius * radius

# Основна програма
def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = int(input("Введіть ваш вибір (1/2/3): "))

    if choice == 1:
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        print(f"Площа прямокутника: {area_of_rectangle(length, width):.2f}")
    
    elif choice == 2:
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        print(f"Площа трикутника: {area_of_triangle(base, height):.2f}")
    
    elif choice == 3:
        radius = float(input("Введіть радіус кола: "))
        print(f"Площа кола: {area_of_circle(radius):.2f}")
    
    else:
        print("Неправильний вибір! Оберіть 1, 2 або 3.")

if __name__ == "__main__":
    main()
