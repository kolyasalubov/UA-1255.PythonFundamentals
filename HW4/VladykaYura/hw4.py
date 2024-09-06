user_temperature = float(input("Enter the temperature in Celsius:"))


if user_temperature < -273.15:
    print("Error:temperature below absolute zero(-273.15)")
else:
    temperature_fahrenheit = user_temperature * (9/5)+32
    print(f"{user_temperature}C is equivalent to {temperature_fahrenheit}F")    

