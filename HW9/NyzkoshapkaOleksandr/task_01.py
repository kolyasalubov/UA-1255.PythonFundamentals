from random import randint

genereted_number = randint(1,100)
print(genereted_number)
tries = 1
while tries < 11:
    guess_number = int(input("What number is your guess?: "))
    if guess_number == genereted_number and 1 <= tries <=3:
        print(f"Congratulations, you guessed it! You must be a Wanga! The number is {genereted_number}")
        break
    elif tries == 10 and guess_number != genereted_number:
        print ( f"Unfortunately, you didn't guess... Try next time! Good luck!!! The number was {genereted_number}" ) 
    elif guess_number == genereted_number:
        print(f"Congratulations, you guessed it! The number is {genereted_number}")
        break
    elif guess_number != genereted_number and guess_number < genereted_number :
        print(f"Ooopss... Unfortunately, you did not guess. But I have a tip - take it higher. I believe in you!!! {10-tries} tries ")
    elif guess_number != genereted_number and guess_number > genereted_number :
        print(f"Ooopss... Unfortunately, you did not guess. But I have a tip - sometimes it's worth landing. I believe in you!!! {10-tries} tries ")   
    tries += 1