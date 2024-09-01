number = int(input("Введіть чотиризначне натуральне число: "))

digits = [int(digit) for digit in str(number)]

product_of_digits = digits[0] * digits[1] * digits[2] * digits[3]

reversed_number = int(str(number)[::-1])

sorted_digits = sorted(digits)
sorted_number = int("".join(map(str, sorted_digits)))

print(f"Добуток цифр: {product_of_digits}")
print(f"Число у зворотному порядку: {reversed_number}")
print(f"Цифри, відсортовані у зростаючому порядку: {sorted_number}")
