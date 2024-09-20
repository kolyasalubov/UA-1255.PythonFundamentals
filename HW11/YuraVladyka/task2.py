def my_code():
    
    
    try:
        choice = int(input("Enter number: "))
    except ValueError:
        raise ValueError("Error: Please enter a valid number.")

    
    if choice < 1:  
        raise ValueError("Error: Number must be positive.")
    week = ["Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday", 
            "Saturday", 
            "Sunday"]
   
    return(week[choice-1])
try:
    print(my_code())
except IndexError:
    print("Error:Enter 1 to 7")
except ValueError as e:
    print (e)