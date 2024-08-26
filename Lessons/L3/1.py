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
name = "John"
age = 23
salary = 999.99
print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))
