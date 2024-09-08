number = 3527

num_str = str(number)

digit1 = int(num_str[0])
digit2 = int(num_str[1])
digit3 = int(num_str[2])
digit4 = int(num_str[3])

reversed_number = num_str[::-1]

product = digit1 * digit2 * digit3 * digit4

sorted_digits = ''.join(sorted(num_str))

print("Product of the digits", product)
print("Number in reverse order", reversed_number)
print("Digist in ascending order", sorted_digits)