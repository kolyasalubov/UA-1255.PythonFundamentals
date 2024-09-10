temperature_celsius = float(input("Введіть температуру в градусах Цельсія:"))
# Перетворення в градуси Фаренгейта 
temperature_fahrenheit =((temperature_celsius * 9/5)+32)
if temperature_celsius >= -273.15:
    print( f"{temperature_celsius}°C еквівалентно {temperature_fahrenheit} ℉")
else:
    print( f"Помилка:температура нижче абсолютного нуля {temperature_celsius}°C")
    