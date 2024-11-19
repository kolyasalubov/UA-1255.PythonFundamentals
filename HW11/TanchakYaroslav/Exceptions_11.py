# Task 1
class NegativeNumber(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(f"Negative number: {self.data}")

def even_odd_age(age):
    if age < 0:
        raise NegativeNumber("you entered negative number instead of positive")
    elif age % 2 == 0:
        print("Age is even")
    elif age % 2 == 1:
        print("Age is odd")
loop_condition = True
while loop_condition:
    try:
        age = int(input("Enter your age, please - "))
        even_odd_age(age)
    except NegativeNumber as error:
        loop_condition = False
        print(repr(error))


# Task 2

def check_number(num):
    if week_day_number < 0 or week_day_number > 7:
        raise IndexError("Unfortunately, there is no such number of days of the week")

def check_value(value):
    if not isinstance(week_day_number, int):
        raise ValueError
# tuple_day_of_week_negative = ("Sunday", "Saturday", "Friday", "Thursday", " Wednesday", "Tuesday","Monday")
tuple_day_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

loop_condition = True
print("""Choose your favorite week day
0 - Exit
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday
7 - Sunday""")
while loop_condition:
    try:
        week_day_number = int(input("Enter the number of the week day - "))
        if week_day_number == 0:
            print("Goodbye, see you later! ;)")
            break
        check_number(week_day_number)
        check_value(week_day_number)
        print(tuple_day_of_week[week_day_number-1])
        # print(tuple_day_of_week_negative[-week_day_number])
    except (ValueError, IndexError) as error:
        print(repr(error))

