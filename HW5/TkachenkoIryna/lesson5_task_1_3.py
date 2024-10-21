print('Task_1')
''' Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).'''

number = int(input('Enter amount of numbers: '))
list_number = []
for item in range(number):
    list_number.append(float(input('Enter your next numbers: ')))
print(list_number)

# list_int = [56, 172, 19, 54]
# for item in range(len(list_int)):
#     list_int[item] = float(list_int[item])
# print(list_int)

print()
print('Task_2')
'''Print Fibonacci numbers up to the entered number n,
using cycles.'''
n = int(input('Enter the number to stop Fibonacci numbers before it: '))
a, b = 0, 1
while a <= n:
    print(a, end=' ')
    a, b = b, a + b

print()
print('Task_3')
'''Write a script that will calculate the factorial of the entered
number without using recursion'''
number = int(input('Enter a number to calculate its factorial: '))
if number == 0:
    print(1)
elif number < 0:
    print('The factorial of negative numbers does not exist')
else:
    factorial = 1
    for item in range(1, number + 1):
        factorial *= item
    print(factorial)
