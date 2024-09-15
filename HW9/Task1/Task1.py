import random

digits_random = random.randint(1, 100)

#print("Random number (for testing purposes):", digits_random)

i = 0

while i < 10:
    digits= int(input("Enter digits:"))
    if digits == digits_random:
        print("You guessed the number")
    elif i<9:
        if digits<digits_random:
            print(f"Number > {digits}")
            print(f"Try again , you have {9-i} attempt")
            i = i+1
        else :
            print(f"Number < {digits}")
            print(f"Try again , you have {9-i} attempt")
            i = i+1
    else:
        print("The end")
    
        