# WeatherApp v.0.0.1

WeatherApp is a Python application that allows users to fetch and display weather information for a specific city using the OpenWeatherMap API. It features a graphical user interface (GUI) built with the Tkinter library.

## Features

- Retrieve current weather data for a specified city.
- Display temperature, feels-like temperature, pressure, humidity, wind speed, sunrise, sunset, cloud cover, and weather description.
- Handle cases where weather data for a city is not found.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- An API key from OpenWeatherMap. (Sign up and obtain your API key [here](https://home.openweathermap.org/users/sign_up).)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/WeatherApp.git
```
2. Change into the project directory:
```bash
cd WeatherApp
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Create a .env file in the project directory and add your OpenWeatherMap API key:
```plaintext
WEATHER_API_KEY=your_api_key_here
```

## Usage
1. Run the WeatherApp by executing the main script:
```bash
python main.py
```
2. The application window will open, prompting you to enter a city name.
3. Click the "Check Weather" button to fetch and display weather information for the entered city.

## Libraries Used
* tkinter: For creating the graphical user interface.
* requests: For making HTTP requests to the OpenWeatherMap API.
* dotenv: For loading environment variables from the .env file.
* datetime: For formatting time data.

## Project Structure
* main.py: The main entry point of the application.
* README.md: This documentation file.
* requirements.txt: List of required Python packages.
## License
This project is licensed under the MIT License.


