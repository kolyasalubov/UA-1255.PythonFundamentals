# Program 2
your_number = input('Введіть ціле чотиризначне число: ')
if len(your_number) != 4:
    print('Це не чотиризначне число!')
else:
    first_digit = int(your_number) // 1000 
    second_digit = (int(your_number) - first_digit * 1000) // 100
    third_digit = (int(your_number) - first_digit * 1000 - second_digit * 100) // 10
    fourth_digit = int(your_number) - first_digit * 1000 - second_digit * 100 - third_digit * 10
    
    #print(first_digit,second_digit,third_digit,fourth_digit)
    product_of_digits = first_digit * second_digit * third_digit * fourth_digit
    print('Добуток всіх цифр у числі рівний:', product_of_digits )
    
    reversed_number = fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
    print(f'Число {your_number} задом наперед:', reversed_number)

    sorted_digits = ''.join(sorted(your_number))
    print(f"Цифри у порядку зростання: {sorted_digits}")
    