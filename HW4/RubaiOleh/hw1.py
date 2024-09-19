def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Error: Temperature below absolute zero (-273.15°C)"
    else: 
        fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}C дорівнє {fahrenheit}F"

celsius = float(input("Enter temperature in celsius"))
result = celsius_to_fahrenheit(celsius)
print(result)
    