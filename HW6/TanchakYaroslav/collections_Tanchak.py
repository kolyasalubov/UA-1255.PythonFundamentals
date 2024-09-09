# Task 1
divisible_2 = []
divisible_3 = []
except_2_and_3 = []

for i in range(1,11):
    if i % 2 == 0:
        divisible_2.append(i)
    elif i % 3 == 0:
        divisible_3.append(i)
    else:
        except_2_and_3.append(i)
print(f"{divisible_2 = } \n{divisible_3 = } \n{except_2_and_3 = }")

# Task 2

login = input("Enter your login, please - ")

while login != "First":
    print("Login is incorrect, please try again")
    login = input("Enter your login, please - ")
else:
    print("Welcome to the club, buddy")
