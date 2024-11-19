class CustomError(Exception):
    
    def __init__(self, data) :
        self.data = data

    def __str__(self) :
        return repr(f"My repr: {self.data}")


try:
    age = int(input("Please input your age: "))
    if age < 0 :
        raise CustomError("Some exception: negative number, unfortantly we are not getting any younger")
    print("Age is even") if int(age) % 2 == 0 else print("Age is odd")
    
except (CustomError,ValueError) as e:
    print("Sorry invalid age!", e)

