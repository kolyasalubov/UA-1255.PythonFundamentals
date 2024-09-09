number = int(input("Введіть число для обчислення його факторіалу: "))

factorial = 1

if number == 0 or number == 1:
    factorial = 1
else:
    for i in range(2, number + 1):
        factorial *= i

print(f"Факторіал числа {number} дорівнює {factorial}")
