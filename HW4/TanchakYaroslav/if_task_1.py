# Task 1 - Temperature Converter

temperature = int(input("Enter the temperature in Celsius - "))

if temperature < -273.15:
    print("Incorrect temperature")
    print("It`s below absolute zero, -273.15")
elif temperature >= -273.15:
    F = (temperature * (9/5) + 32)
    print(f"Celsius = {temperature} \nFahrenheit = {round(F,1)}")