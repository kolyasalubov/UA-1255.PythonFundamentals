
even_list = []
odd_list = []
other_list = []
for item in range (11):
    if item % 2 == 0 :
        even_list.append(item)
    elif item % 3 == 0:
        odd_list.append(item)
    else : other_list.append(item)
print( even_list)
print(odd_list)
print(other_list)

#list comprehension
even_list = [item for item in range (11) if item % 2 == 0]
odd_list = [item for item in range (11)  if item % 3 == 0]
other_list = [item for item in range(11) if item % 2 != 0 and item % 3 != 0 ]

print( even_list)
print(odd_list)
print(other_list)