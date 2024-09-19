number = input('Enter the number: ')
dobutok = 1

if len(number) != 4:
    print('the number is not four digits')
else:
    for digit in number:
        dobutok *= int(digit) 
    print('Добуток чисел - ', dobutok)

number_in_reverse_order = int((number)[::-1])
print('number in reverse order - ', number_in_reverse_order)

sorted_number = ''.join(sorted(number))
print('Числа за зростанням - ', sorted_number)