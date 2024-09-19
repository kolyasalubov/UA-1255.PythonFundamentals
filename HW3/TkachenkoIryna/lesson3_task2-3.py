print("Task_2")
# find the product of the digits of this number
number = 4279
print(f"Number is {number}")
number_to_string = str(number)
list_from_number = list(number_to_string)
expression = "*".join(list_from_number)
evaluation = eval(expression)
print(f"The product of the digits of this number is {evaluation}")

# write the number in reverse order
number_reversed = number_to_string[::-1]
print(f"The reverse number to {number_to_string} is {number_reversed}")

# in ascending order, you need to sort the numbers included in the given number
numbers_ascending_list = sorted(list_from_number)
numbers_ascending_separate = ", ".join(numbers_ascending_list)
numbers_ascending_joined = "".join(numbers_ascending_list)
print(f"Numbers, sorted ascending, are: \n"
      f"{numbers_ascending_separate} or \n"
      f"{numbers_ascending_joined}")
print()  # This print is for a blank line
print("Task_3")
# Interchange the values ​of two variables without using the third variable.
first_var = "first"
second_var = "second"
first_var, second_var = second_var, first_var
print(f"""When interchanged:
      First variable is {first_var} and
      second variable is {second_var}.""")
