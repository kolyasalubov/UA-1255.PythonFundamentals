numbers = range(1, 11)

even_numbers_divisible_by_2 = [num for num in numbers if num % 2 == 0]

odd_numbers_divisible_by_3 = [num for num in numbers if num % 2 != 0 and num % 3 == 0]

not_divisible_by_2_and_3 = [num for num in numbers if num % 2 != 0 and num % 3 != 0]

print("Even numbers divisible by 2:", even_numbers_divisible_by_2)
print("Odd numbers divisible by 3:", odd_numbers_divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_and_3)