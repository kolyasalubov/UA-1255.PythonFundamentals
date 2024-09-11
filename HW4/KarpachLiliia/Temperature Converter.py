user_input = int(input('Enter the temperature in Celsius:'))
if user_input < -273.15:
    print('Error: Temperature below absolute zero (-273.15\u00B0C)')
else:
    temperature_fahrenheit = user_input * (9/5) + 32
    print(f'{user_input}\u00B0C is equivalent to {temperature_fahrenheit}\u00B0F')
