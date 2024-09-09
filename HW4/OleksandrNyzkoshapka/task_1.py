temperature_in_Celsius = float(input("Enter the temperature in Celsius: "))
temperature_in_Fahrenheit = int((temperature_in_Celsius * 9/5) + 32)
print("Error: Temperature below absolute zero (-273.15°C)" if temperature_in_Celsius < -273.15 else f"{int(temperature_in_Celsius)}°C is equivalent to {temperature_in_Fahrenheit}°F")
