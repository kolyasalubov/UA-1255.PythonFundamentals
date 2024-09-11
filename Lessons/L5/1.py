# # # # d = (89, 78.5, "hello")
# # # # print(d[0])
# # # # print(id(d))
# # # # d[0]= 777
# # # # print(d)


# # # ########################


# # # squares = {}
# # # for x in range(6):
# # #     if x%2==0:
# # #         squares[x] = x*x

# # # print(squares)

# # # sq = {x: x*x for x in range(6) if x%2==0}
# # # print(sq)

# # def print_message(name_user):
# #     """
# #     Docstring
# #     input param: name_user,
# #     type input peram: str
# #     return param: str  
# #     """
# #     return f"Hello, {name_user}"
# #     print("Hello")



# # s = print_message("Liubov")
# # # print_message("Helen")

# # print(s, type(s), print_message.__doc__)

# ################################################
# def my_sum(arg1 = 90, arg2):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
    


# suma = my_sum(1, 4)
# print("Outside the function : ", suma)

##########################################

def print_info(name, age = 18):
    print("Name: ", name)
    print("Age: ", age)

print_info("Alex")
print("-" * 10)
print_info(25, "Ogi")

