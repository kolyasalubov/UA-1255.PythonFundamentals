number = int(input('Enter the number: '))

first_number = 0
mate_number = 1

print(first_number, end = '')

while mate_number <= number:
    print(mate_number, end = '')
    first_number,mate_number = mate_number, first_number + mate_number
    

