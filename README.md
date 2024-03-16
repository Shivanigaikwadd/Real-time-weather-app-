# Real-Time Weather App

This is a simple Streamlit web application that displays real-time weather data based on user-provided latitude and longitude.

## Features

- Users can input latitude and longitude to get real-time weather data.
- The app fetches weather data (temperature, humidity, rainfall, and snowfall) from the OpenWeatherMap API.
- Displays the retrieved data in a clear and organized manner within the app.

## Getting Started

To run this app locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain an API key from OpenWeatherMap and insert it into the `main()` function in `weather_app.py`.
4. Run the Streamlit app by executing `streamlit run weather_app.py` in your terminal.

## Usage

1. Enter the latitude and longitude coordinates in the input fields.
2. Provide your OpenWeatherMap API key.
3. Click on the "Get Weather Data" button to retrieve real-time weather information.

## Dependencies

- Streamlit
- Requests
- Geopy


