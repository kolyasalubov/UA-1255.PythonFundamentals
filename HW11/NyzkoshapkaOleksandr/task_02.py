class CustomError(Exception):
    
    def __init__(self, data) :
        self.data = data

    def __str__(self) :
        return repr(f"My repr: {self.data}")
    
try:

    
    week = {1: "Monday", 2: "Tuesday", 3: "Wensday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday" }
    input_number = int(input("Please input number 1-7: "))
    if input_number > 7:
        raise CustomError( "Some exception: There are seven days in week ")
    elif input_number < 0:
        raise CustomError("Some exception: negative number")
    for keys in week:
        if input_number in week:
            print (week[input_number])
        break

except (CustomError, ValueError) as e:
    print("Sorry invalid value!", e)