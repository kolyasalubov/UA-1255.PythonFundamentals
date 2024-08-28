# user_name1 = "Liubov"
# user_name2 = "Liubov"
# print(user_name1, type(user_name2), id(user_name1))
# print(user_name2, type(user_name2), id(user_name2))
# # PI = 3.14
# # print(PI)
# # PI = 900
# # print(PI, type(PI))
#############################################################



# x = 'foo'
# y = x
# print (id(x), x) # foo
# print (id(y), y)
# y = y + "bar"
# print("y", y, id(y))
# print("x", x, id(x))


# x = [1, 2, 3]
# y = x
# print ("x", id(x), x) 
# print ("y", id(y), y)

# y += [3, 2, 1]
# print ("x", id(x), x) 
# print ("y", id(y), y)

# f = r"raw\name\table"
# f2 = "raw\name\table"
# print(f)
# print(f2)

# This prints out "John is 23 years old. Your sallary is 999.990 $"
# name = "John"
# age = 23
# salary = 999.99
# print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))

# a = 90
# b = 89
################################################################

# l = [23, 90]
# print(l)
# l.append(78)
# print(l)

# name_1 = 'John'
# name_2 = 78
# name_3 = 'Sean'

# # default(implicit) order
# default_order = "Hello {}, {} and {}".format(name_1, name_2, name_3)
# print(default_order)
# # # order using positional argument
# positional_order = "Hello {1}, {0} and {2}".format('John','Bill','Sean')
# print(positional_order)
# # # order using keyword argument
# keyword_order = "Hello {s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# print(keyword_order)

#################################

# name_1 = 'John'
# name_2 = 78
# name_3 = 'Sean'

# default_order = f"Hello {name_2}, {name_1} and {name_3}"
# print(default_order)

my_str = 'programiz'
# print('str = ', my_str, id(my_str))
# print(my_str[-2])
# d = my_str[:]
# print(d)
print('str[5:-2] = ', my_str[5:-2])

