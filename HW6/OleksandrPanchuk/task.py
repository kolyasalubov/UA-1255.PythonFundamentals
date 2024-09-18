# Task 1
numbers = [x for x in range(1, 11)]
evennumbers = [x for x in numbers if x % 2 == 0]
oddnumbers = [x for x in numbers if x % 3 == 0]
numbers_not_divisible_by_2_and_3 = [x for x in numbers if x % 2 != 0 and x % 3 != 0]

print(f"Even numbers: {evennumbers}")
print(f"Odd numbers: {oddnumbers}")
print(f"Numbers not divisible by 2 and 3: {numbers_not_divisible_by_2_and_3}")

# Task 2
Flag = True
while Flag:
    login = input("Enter your login: ")
    if login == "First":
        print("Hello, First!")
        Flag = False
    else:
        print("Incorrect login, try again")