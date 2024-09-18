import tkinter as tk
from tkinter import font
from pyowm import OWM
from cofigure import API_KEY
# API Key for OWM

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Основні розміри вікна
HEIGHT = 350
WIDTH = 450

# Функція для отримання погоди за назвою міста
def get_weather():
    city = entry_field.get()  # Отримуємо введене місто
    try:
        observation = mgr.weather_at_place(city)  # Шукаємо погоду в місті
        w = observation.weather

        # Отримуємо різні параметри погоди
        description = w.detailed_status
        temp = w.temperature('celsius')['temp']
        wind_speed = w.wind()['speed']
        humidity = w.humidity
        clouds = w.clouds
        
        # Формуємо текст для відображення
        final_str = f"City: {city}\nConditions: {description}\nTemperature (°C): {temp}\n" \
                    f"Wind Speed: {wind_speed} m/s\nHumidity: {humidity}%\nClouds: {clouds}%"
    except:
        final_str = "There was a problem retrieving that information."

    # Оновлюємо текст у вікні результату
    label['text'] = final_str

# Основний код для створення вікна
root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Верхня панель для введення назви міста та кнопки
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="white", font=('Courier', 8), command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Нижня панель для відображення результатів
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
