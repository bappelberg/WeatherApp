# Import internal modules
from datetime import datetime
import json
import os
import http.client
import tkinter as tk

# Import external modules
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the weather API key from environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# WeatherApp class represents the main application
class WeatherApp:
    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()
        self.root.geometry("800x400")
        self.root.title("WeatherApp")

        # Variable to hold the entered city name
        self.city_name_var = tk.StringVar()

        # Create and place GUI elements
        self.city_label = tk.Label(
            self.root, text="Enter city name", font="Arial 12 bold"
        )
        self.city_entry = tk.Entry(
            self.root, textvariable=self.city_name_var, width=24, font="Arial 14 bold"
        )

        self.city_label.pack()
        self.city_entry.pack()

        # Initialize instances of WeatherFetcher and WeatherDisplayer
        self.weather_fetcher = WeatherFetcher()
        self.weather_displayer = WeatherDisplayer(self.root)

        # Create and place the weather display button
        self.weather_btn = tk.Button(
            self.root,
            command=self.display_weather,
            text="Check Weather",
            font="Arial 10",
            bg="lightblue",
            fg="black",
            activebackground="teal",
            padx=5,
            pady=5,
        )
        self.weather_btn.pack(pady=10)

        # Start the main event loop
        self.root.mainloop()

    # Function to display weather information for the entered city
    def display_weather(self):
        city_name = self.city_name_var.get()
        weather_data = self.weather_fetcher.fetch_weather_data(city_name)
        self.weather_displayer.display(city_name, weather_data)


# WeatherFetcher class handles fetching weather data from an API
class WeatherFetcher:
    # Function to fetch weather data for a given city name
    def fetch_weather_data(self, city_name):
        host = "api.openweathermap.org"
        url = f"/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}"
        conn = http.client.HTTPConnection(host)
        conn.request(
            "GET",
            url,
            headers={"Host": host},
        )

        response = conn.getresponse()

        if response.status == 200:
            response_content = response.read()
            weather_data = json.loads(response_content)
            return weather_data
        else:
            return None


# Function to format time for a specific location
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


# WeatherDisplayer class manages displaying weather information
class WeatherDisplayer:
    def __init__(self, root):
        self.KELVIN = 273.15
        self.text_widget = tk.Text(root, width=45, height=16)
        self.text_widget.pack()

    # Function to display weather information in the GUI
    def display(self, city_name, weather_data):
        self.text_widget.delete("1.0", "end")
        if weather_data:
            weather_info = self.get_weather_info(weather_data)
            self.text_widget.insert(
                "1.0", f"Current weather for city: {city_name}\n\n{weather_info}"
            )
        else:
            error_message = f'\n\tWeather for "{city_name}" was not found! Please enter a valid city name.'
            self.text_widget.insert(tk.INSERT, error_message)

    # Function to extract and format weather information
    def get_weather_info(self, weather_data):
        celsius = int(weather_data["main"]["temp"] - self.KELVIN)
        feels_like_celsius = int(weather_data["main"]["feels_like"] - self.KELVIN)
        pressure = weather_data["main"]["pressure"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        sunrise = weather_data["sys"]["sunrise"]
        sunset = weather_data["sys"]["sunset"]
        timezone = weather_data["timezone"]
        cloudy = weather_data["clouds"]["all"]
        description = weather_data["weather"][0]["description"]

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather_info = f"Celsius: {celsius}°\nFeels like: {feels_like_celsius}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nWind speed: {wind_speed} m/s\nDescription: {description}"

        return weather_info


# Entry point of the program
if __name__ == "__main__":
    app = WeatherApp()
