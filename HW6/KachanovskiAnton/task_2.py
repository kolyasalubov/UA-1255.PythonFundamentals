user_login = ""

while user_login != "First":
    user_login = input("Enter your login: ")
    if user_login == "First":
        print("Greetings, First!")
    else:
        print("Error: Incorrect login, please try again.")