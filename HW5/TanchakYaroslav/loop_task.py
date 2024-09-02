# Task 1
# list_numbers = [23, 45, 71, 12, 516, 3, 57, 10]
#
# for i in range(len(list_numbers)):
#     list_numbers[i] = float(list_numbers[i])

# Task 2

# Version 1
# fibonacci_list = [0, 1]
# numb_fibonacci = int(input("Enter number for sequence of Fibonacci, please - "))
#
# for i in range(abs(numb_fibonacci)):
#     next_fib_numb = fibonacci_list[-2] + fibonacci_list[-1]
#     if next_fib_numb > numb_fibonacci:
#         break
#     fibonacci_list.append(next_fib_numb)
#
# print(fibonacci_list)

#Version 2
fibonacci_list = [0, 1]
numb_fibonacci = abs(int(input("Enter number for sequence of Fibonacci, please - ")))

while True:
    next_fib_numb = fibonacci_list[-2] + fibonacci_list[-1]
    if next_fib_numb > numb_fibonacci:
        print("Next number for sequence of Fibonacci is higher than entered")
        print("Sequence of Fibonacci is ready - ", fibonacci_list)
        break
    fibonacci_list.append(next_fib_numb)


# Task 3

# numb_factorial = int(input("Enter number for factorial, please - "))
# factorial = 1
#
# for i in range(1, numb_factorial+1):
#     factorial *= i
# else:
#     print(factorial)



