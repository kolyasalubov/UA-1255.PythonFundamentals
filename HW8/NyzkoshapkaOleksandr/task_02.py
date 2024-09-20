import re



def error():
    print("Your password is invalid")

def Check_Password(user_password):
     result = re.findall(r"[A-Z]", user_password)
     if result != None :
         result = re.findall(r"[a-z]",user_password)
         if result != None :
             result = re.findall(r"\d", user_password)
        
             if result != None :
                 result = re.findall(r"[$#@]", user_password)
                 if result != None :
                     if 6 <= len(user_password) <=16 :
                         print("Your passwor is valid")
                     else: error()
                 else: error()
         else: error()

                 
     else: error()
        
user_password = input("Input your password: ")
Check_Password(user_password)
