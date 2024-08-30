four_digit_natural_number = input("Enter a four-digit natural number: ")

if len(four_digit_natural_number) != 4:
    print("Please enter a valid four-digit natural number.")
    four_digit_natural_number = input("Enter a four-digit natural number: ")
else:
    digits = [int(digit) for digit in four_digit_natural_number]

    product = 1
    for digit in digits:
        product *= digit

    reversed_number = four_digit_natural_number[::-1]

    sorted_digits = ''.join(sorted(four_digit_natural_number))

    print(f"Product of the digits of this number: {product}")
    print(f"Number in reverse order: {reversed_number}")
    print(f"Digits of the number in ascending order: {sorted_digits}")