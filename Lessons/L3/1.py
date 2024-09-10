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

# my_str = 'programiz'
# print('str = ', my_str, id(my_str))
# print(my_str[-2])
# d = my_str[:]
# print(d)
# print('str[5:-2] = ', my_str[5:-2])

# x = 10
# y = 12

# print("x > y is", x > y)
# print("x < y is", x < y)
# print("x == y is", x == y)
# print("x != y is", x!= y)

# Identity operators

# x1 = 5
# y1 = 5
# x2 = "Hello"
# y2 = "Hello"
# x3 = [1,2,3]
# y3 = [1,2,3]

# print(x1 is not y1)
# print(x2 is y2)
# print(x3 is y3)

# a = 2
# b = 2

# print(a is b)
# print(id(a))
# print(id(b))

# l1 = []
# l2 = []

# print(l1 is l2)
# print(id(l1))
# print(id(l2))

# x = "Hello world"
# y = {1: "a", 2: "b"}

# print("H" in x)
# print("hello" not in x)
# print(1 in y)

# score = 12

# if score > 8:
#     print("You have passed the exam")
# print("Exam was finished.")

# score = float(input("What score? "))
 
# if score >= 90:
#     print('A')
# else:
#  if score >= 80:
#     print('B')
# else: # grade must be C, D or F
#    if score >= 70:
#     letter = 'C'
# else: # grade must D or F
# if score >= 60:
#     letter = 'D'
# else: letter = "F"

# variable_1 = 1
# variable_2 = 2
# variable_3 = "3"

# print(variable_1 + variable_2 + variable_3)

# value = 36 / 4 * (3 + 2) * 4 + 2
# print(value)

# value1 = 5 ** 2
# value2 = 5 ** 3

# print(value1, value2)

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# p, q, r = 10, 20, 30
# print(p, q, r)

# print(type({}) is set)

# s1 = "hot"
# s2 = "dog"
# print(s1 + s2)

# str1 = "my isname isisis jameis isis bond"
# sub = "is"
# print(str1.count(sub, 4))

# print("John" > "Jhon")
# print("Emma" < "Emm")

# str1 = "My salary is 7000";
# str2 = "7000"

# print(str1.isdigit())
# print(str2.isdigit())

# Select the correct output of the following String operations

# str1 = 'Welcome'
# print(str1*2)

# str = "my name is James bond"
# print (str.capitalize())

# first_name = "television"
# hobby = "homer"
# tmp = first_name
# first_name = hobby
# hobby = tmp
# print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")

# if False:
#     print("Nissan")
# elif True:
#     print("Ford")
# elif True:
#     print("BMW")
# else:
#     print("Audi")

# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#     print('False')

# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# if 2 == 2:
#     print("ice cream is tasty!")

# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# if "cat" == "dog":
#     print("prrrr")
# else:
#     print("ruff")

# def count_digits(n):
#     if not isinstance(n, int):
#         print("Wrong data type")
#         return
#     n = abs(n)
#     digit_count = len(str(n))
#     return digit_count

# print(count_digits(123))
# print(count_digits(-23))
# print(count_digits("abc"))

# temp_celsius = float(input("Enter the temperature in C°:"))
# temp_fahrenheit = temp_celsius * 9/5 + 32


# if temp_celsius < -273.15:
#   print("Temperature is invalid because it is below absolute zero")

# else:
#   print(f"The temperature in Fahrengeit is {temp_fahrenheit}:")