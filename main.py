import tkinter as tk
from tkinter import font
import requests
from io import BytesIO
from PIL import Image, ImageTk

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
        icon_code = weather_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        icon_response = requests.get(icon_url)
        icon_image = Image.open(BytesIO(icon_response.content))
        icon_image = icon_image.resize((100, 100), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)


        result_label.config(text=f"Temperature: {temperature}°C\nDescription: {weather_desc}")
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo
    else:
        result_label.config(text="City not found")
        icon_label.config(image="")



window = tk.Tk()
window.title("Weather App")

window_width = 400
window_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

header_font = font.Font(family="Arial", size=16, weight="bold")
body_font = font.Font(family="Arial", size=12)

city_entry = tk.Entry(window, width=50, font=("Arial", 14))
city_entry.pack(pady=10)

get_weather_button = tk.Button(window, text="Show weather", command=get_weather, width=20)
get_weather_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

icon_label = tk.Label(window)
icon_label.pack(pady=10)

window.mainloop()