def largest_number(num1, num2):
    """
    Returns the largest of two numbers.
    
    Parameters:
    num1 (int, float): The first number to compare.
    num2 (int, float): The second number to compare.
    
    Returns:
    int, float: The largest number between num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2

try:
    user_first_number = float(input("Enter first number: "))
    user_second_number = float(input("Enter second number: "))
    
    result = largest_number(user_first_number, user_second_number)
    print(f"Largest number is {result}")
except ValueError:
    print("Error: Incorrect number entered.")