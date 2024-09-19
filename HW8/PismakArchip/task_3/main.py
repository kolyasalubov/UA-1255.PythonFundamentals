from area_calculations import rectangle_area, triangle_area, circle_area

def main():
    print("Обчислення площі фігур:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = input("Введіть номер фігури, площу якої ви хочете обчислити (1/2/3): ")
    
    if choice == '1':
        a = float(input("Введіть довжину сторони a: "))
        b = float(input("Введіть довжину сторони b: "))
        print(f"Площа прямокутника: {rectangle_area(a, b)}")
        
    elif choice == '2':
        h = float(input("Введіть висоту h: "))
        a = float(input("Введіть довжину основи a: "))
        print(f"Площа трикутника: {triangle_area(h, a)}")
        
    elif choice == '3':
        r = float(input("Введіть радіус кола r: "))
        print(f"Площа кола: {circle_area(r)}")
        
    else:
        print("Неправильний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()