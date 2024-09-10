import tkinter as tk
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Enter city")
        return
    api_key = ("8d7843dc1a4cc5619047da07237dbaed")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        result_label.config(text=f"Temperature: {temperature}°C\nDescription: {weather_desc}")
    else:
        result_label.config(text="City not found")

window = tk.Tk()
window.title("Weather App")

window_width = 300
window_height = 200

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

city_entry = tk.Entry(window, width=50, font=("Arial", 14))
city_entry.pack(pady=10)

get_weather_button = tk.Button(window, text="Show weather", command=get_weather, width=20)
get_weather_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial, 12"), justify="center")
result_label.pack(pady=10)

window.mainloop()