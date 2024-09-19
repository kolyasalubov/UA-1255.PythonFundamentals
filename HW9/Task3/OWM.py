
def get_weather (city):

    from pyowm import OWM


    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------
    #text = input("Enter text")

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details

    observation = mgr.weather_at_place(city)
   
    w = observation.weather

    weather_data = {
        'status': w.detailed_status,       # 'clouds'
        'wind': w.wind(),                  # {'speed': 4.6, 'deg': 330}
        'humidity': w.humidity,            # 87
        'temperature': w.temperature('celsius'),  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        'rain': w.rain,                    # {}
        'heat_index': w.heat_index,        # None
        'clouds': w.clouds                 # 75
    }
    weather_info = (
            f"Status: {weather_data['status']}\n"
            f"Temperature: {weather_data['temperature']['temp']}°C\n"
            f"Humidity: {weather_data['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
            f"Cloud Coverage: {weather_data['clouds']}%\n"
            f"Rain (last hour): {weather_data['rain'].get('1h', 0)} mm"
        )
    return(weather_info) 





