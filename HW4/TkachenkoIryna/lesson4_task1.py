print('Task_1')
# Converter Celsius to Fahrenheit
temperature_Celsius = int(input('Enter the temperature in Celsius: '))
temperature_Fahr = int(temperature_Celsius * 9/5) + 32
degree_sign = '\u00B0'

if temperature_Celsius >= -273.15:
    print(f'{temperature_Celsius}{degree_sign}C is equivalent to {temperature_Fahr}{degree_sign}F')
else:
    print('Error: Temperature below absolute zero (-273,15C)')
