entered_number = int(input("Enter the number for which to calculate the factorial: "))
factorial = 1

for element in range(1, entered_number + 1):
    factorial *= element
else:
    print(f"The factorial of {entered_number} is {factorial}")