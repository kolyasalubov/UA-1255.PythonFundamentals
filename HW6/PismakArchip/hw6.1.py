start = 1
end = 10

even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
odd_numbers_divisible_by_3 = [num for num in range(start, end + 1) if num % 2 != 0 and num % 3 == 0]
numbers_not_divisible_by_2_and_3 = [num for num in range(start, end + 1) if num % 2 != 0 and num % 3 != 0]

print("Парні числа які діляться на 2:",even_numbers)
print("Непарні числа, які діляться на 3:", odd_numbers_divisible_by_3)
print("Числа, які не діляться на 2 і 3:" ,numbers_not_divisible_by_2_and_3)
