def largest_number(num1, num2):
    if num1>num2:
      return num1
    else:
       return num2
    
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(largest_number(num1,num2))