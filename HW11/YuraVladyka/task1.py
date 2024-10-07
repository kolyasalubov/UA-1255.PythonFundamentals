def my_code():
    age=int(input("Enter age:"))
    if age % 2 == 0:
        return("Age is even")
    else:
        return("Age is odd")
try:
 print(my_code())
except ValueError as e:
    print(f"Error: {e}. The entered data is not in the correct format.")
