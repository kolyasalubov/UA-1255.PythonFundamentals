beginning_of_range = 1
ending_of_range = 10

even_numbers_divisible_by_2 = []
odd_numbers_divisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []

for number in range(beginning_of_range, ending_of_range + 1):
    if number % 2 == 0:  # Even numbers divisible by 2
        even_numbers_divisible_by_2.append(number)
    elif number % 3 == 0:  # Odd numbers divisible by 3
        odd_numbers_divisible_by_3.append(number)
    else:  # Numbers not divisible by 2 and 3
        numbers_not_divisible_by_2_and_3.append(number)

print("Even numbers that are divisible by 2:", even_numbers_divisible_by_2)
print("Odd numbers, which are divisible by 3:", odd_numbers_divisible_by_3)
print("Numbers that are not divisible by 2 and 3:", numbers_not_divisible_by_2_and_3)