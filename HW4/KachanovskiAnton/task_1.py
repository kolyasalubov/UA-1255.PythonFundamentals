while True:
    try:
        user_input_temperature = int(input("Enter the temperature in Celsius: "))
        
        if user_input_temperature < -273.15:
            print("Error: Temperature below absolute zero (-273.15)")
            continue

        converted_fahrenheit_temperature = (user_input_temperature * 9/5) + 32
        print(f"{user_input_temperature}°C is equivalent to {converted_fahrenheit_temperature}°F")
        break

    except ValueError:
        print("Error: Please enter a valid number.")