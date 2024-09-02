number = int(input("введіть 4-ьох значне натуральне число"))

digits = [int(digit) for digit in str(number)]

product = 1
for digit in digits:
  product *= digit

reversed_number = int(str(number)[::-1])

sorted_digits = sorted(digits)
sorted_number = int("".join(map(str, sorted_digits)))

print("Добуток цифр:", product)
print("Перевернуте число:", reversed_number)
print("Цифри в порядку зростання:", sorted_number) 