number = input("Enter a four-digit natural number: ")
product_of_digits = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
reversed_number = int(str(number)[::-1])
sorted_number = ''.join(sorted(number))

print(f"Product of digits: {product_of_digits}")
print(f"Reversed number: {reversed_number}")
print(f"Sorted number: {sorted_number}")