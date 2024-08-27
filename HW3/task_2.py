# find the product of the digits of this number
number = 5329
number = str( number)
product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3]) 
print (product)

# write the number in reverse order
sorted_number = sorted(number) 
sorted_number = ''.join(sorted_number)
print (sorted_number)

# in ascending order, you need to sort the numbers included in the given number
reversed_number = number[::-1]
print (reversed_number)