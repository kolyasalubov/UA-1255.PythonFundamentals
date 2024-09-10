# Task 1
list_of_int_numbers = [23,69,52,10,2,54,86,20,21]
list_of_float_numbers = []
for num in list_of_int_numbers:
    list_of_float_numbers.append(float(num))
else:
    print(list_of_float_numbers)

# Task 2
user_input = input("Enter number: ")
numbers = []
Flag = True

while not user_input.isdigit():
    print("This is not a number!")
    user_input = input("Enter number: ")
else:
    while Flag:
        if len(numbers) <= 0:
            numbers.append(0)
        elif len(numbers) == 1:
            numbers.append(1)
        elif numbers[-1] + numbers[-2] > int(user_input):
            Flag = False
        else:
            numbers.append(numbers[-1] + numbers[-2])
    print(numbers)


# Task 3
user_input = input("Enter number: ")

while not user_input.isdigit():
    print("This is not a number!")
    user_input = input("Enter number: ")
else:
    numbers = list(range(1, int(user_input) + 1))
    factorial = 1
    for i in range(1, len(numbers)):
        factorial *= numbers[i]
    else:
        print(f"Factorial of {user_input} is {factorial}")