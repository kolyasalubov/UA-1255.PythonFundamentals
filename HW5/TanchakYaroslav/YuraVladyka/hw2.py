n = int(input("Enter n:")) 
list_number = []
one_number=0
two_number=1


while len(list_number) < n:
    list_number.append(one_number)
    one_number, two_number = two_number, one_number + two_number

print(list_number)