def Password_verification(password):
    import re

    len_password=len(password)
    lowercase_letters = re.findall("[a-z]",password)
    uppercase_letters = re.findall("[A-Z]",password)
    special_characters = re.findall("[$#@]",password)
    digits = re.findall("[1-9]",password)

    if  len_password < 6:
        return("Password contains less than 6 characters")  
    elif len_password > 16:
        return("Password contains more than 16 characters") 
    elif not digits:
        return("there is no digits")
    elif not special_characters:
        return("there is no special characters ")
    elif not lowercase_letters:
        return("there is no lowercase letters")
    elif not uppercase_letters:
        return("there is no uppercase letters")
    else:
        return("Your password accepted")