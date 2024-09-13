def process_number():

  number = int(input("Введіть чотиризначне натуральне число: "))

  digits = [int(digit) for digit in str(number)]

  product = 1
  for digit in digits:
    product *= digit

  reversed_number = int(''.join(map(str, digits[::-1])))

  sorted_digits = sorted(digits)

  print("Product of numbers:", product)
  print("The number is in reverse order:", reversed_number)
  print("Sorted numbers:", sorted_digits)

process_number()