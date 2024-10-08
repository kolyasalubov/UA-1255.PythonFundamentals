import tkinter as tk
from tkinter import font
from pyowm import OWM

# API Key для OpenWeatherMap
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Налаштування OWM
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Функція для отримання погоди
def get_weather():
    place = entry_field.get()
    if place:
        try:
            observation = mgr.weather_at_place(place)
            w = observation.weather
            weather_info = (
                f"Status: {w.detailed_status}\n"
                f"Wind: {w.wind()}\n"
                f"Humidity: {w.humidity}\n"
                f"Temperature: {w.temperature('celsius')}\n"
                f"Rain: {w.rain}\n"
                f"Clouds: {w.clouds}"
            )
            label.config(text=weather_info)
        except Exception as e:
            label.config(text=f"Error: {e}")
    else:
        label.config(text="Please enter a location")

# Налаштування Tkinter
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
