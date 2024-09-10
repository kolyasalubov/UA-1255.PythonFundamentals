# #first variant of realization

# integer_list = [3, 5, 7, 9, 11, 13, 15]
# element = 0

# for element in range(len(integer_list)):
#     integer_list[element] = float(integer_list[element])
# else:
#     print(integer_list)

#second variant of realization using append() as you recommended during class

integer_list = [3, 5, 7, 9, 11, 13, 15]
float_list = []

for element in integer_list:
    float_list.append(float(element))
else:
    print(float_list)