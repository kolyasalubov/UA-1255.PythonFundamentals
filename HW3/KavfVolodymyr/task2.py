number = input("Enter a four digit number")

print(f'The product of numbers is: {int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])}')

print(f'Reversed number: {number[::-1]}')

print(f'Sorted list: {list("".join(sorted(number)))}\n')
