even_numbers =[]
odd_numbers =[]
number_other = []

for number in range(1,11):
    if number % 3 ==0:
      odd_numbers.append(number) 
     
    elif number % 2 == 0:
        even_numbers.append(number) 
    else:
        number_other.append(number)
        
print("Parne :",even_numbers)
print("Unparne :",odd_numbers)
print("Other :",number_other)