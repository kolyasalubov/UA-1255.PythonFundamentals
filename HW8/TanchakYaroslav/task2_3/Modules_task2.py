# Task 2 - Password Validation
# Version 1 - without module re
# Цю версію програми я написав до того як дойшов до моменту про регулярні вирази
# Я думав як її оптимізувати але не поки не зміг нічого кращого придумати
#
import re

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
symbols = "@#$"

def password_validation(input_password):
    if len(input_password) >= 6 and len(input_password) <= 16:
        for i in input_password:
            if i in alphabet_lower:
                break
        else:
            return True, "You need stronger password, add at least one any letter in lower case"
        for i in input_password:
            if i in alphabet_upper:
                break
        else:
            return True, "You need stronger password, add at least one any letter in upper case"
        for i in input_password:
            if i in symbols:
                break
        else:
            return True, "You need stronger password, add at least one of these symbols @, #, $"
        for i in input_password:
            if i in digits:
                break
        else:
            return True, "You need stronger password, add at least one any digit"
    else:
        return "Your password is too short, it has to be at least 6 characters and not more than 16 characters"
    return False, "Password is valid"

input_password = None
loop_condition = True,
while loop_condition[0]:
    input_password = input("Enter your password, please: ")
    loop_condition = password_validation(input_password)
    if loop_condition[0]:
        print(loop_condition[1])
else:
    print(loop_condition[1].center(31, "*"))


# Version 2 - with module re
# В цій версії можна ще було піти від зворотнього
# Не робити вкладені умовні оператори а використати elif not
# Тоді коду би мало би бути трохи менше

# def password_validation(input_password):
#     if len(input_password) >= 6 and len(input_password) <= 16:
#         if re.search("[a-z]", input_password):
#             if re.search("[A-Z]", input_password):
#                 if re.search("[0-9]", input_password):
#                     if re.search("[@#$]", input_password):
#                         return False, "Password is valid"
#                     else:
#                         return True, "You need stronger password, add at least one of these symbols @, #, $"
#                 else:
#                     return True, "You need stronger password, add at least one any digit"
#             else:
#                 return True, "You need stronger password, add at least one any letter in upper case"
#         else:
#             return True, "You need stronger password, add at least one any letter in lower case"
#     else:
#         return True, "Your password is too short, it has to be at least 6 characters and not more than 16 characters"
#
# input_password = None
# loop_condition = True,
# while loop_condition[0]:
#     input_password = input("Enter your password, please: ")
#     loop_condition = password_validation(input_password)
#     if loop_condition[0]:
#         print(loop_condition[1])
# else:
#     print(loop_condition[1].center(20, "*"))

    