def counting_letters(string):
    len_string=len(string)
    my_dict = {}
    i=0
    while i<len_string:
        if string[i] in my_dict:
           my_dict[string[i]] +=1
           
        else:
            my_dict[string[i]] = 1
        i=i+1

    return (my_dict)

string = input("Enter string:")
print("Result:",counting_letters(string))   