import random

def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 10

    print("Ласкаво просимо до гри!")
    print("Я вибрав число від 1 до 100.")
    print("У вас є 10 спроб, щоб вгадати його.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}: Введіть ваше припущення: "))
            
            if guess < target_number:
                print("Число більше.")
            elif guess > target_number:
                print("Число менше.")
            else:
                print("Вітаємо! Ви вгадали число!")
                break
        except ValueError:
            print("Будь ласка, введіть дійсне число.")
        
        if attempt == attempts:
            print(f"На жаль, ви використали всі спроби. Число було {target_number}.")

guessing_game()
