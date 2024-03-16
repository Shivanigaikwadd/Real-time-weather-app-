import streamlit as st
import requests
from geopy.geocoders import Nominatim

def get_location(latitude, longitude):
    geolocator = Nominatim(user_agent="Real-Time Weather App")
    try:
        location_info = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location_info:
            address = location_info.address
            return address
        else:
            return None
    except:
        return None

def get_weather_data(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert temperature from Kelvin to Celsius
        humidity = data['main']['humidity']
        # Check if 'rain' key exists in the response
        if 'rain' in data:
            rainfall = data['rain'].get('1h', 0)  # Get rainfall in the last hour (if available), default to 0 if not available
        else:
            rainfall = 0
        # Check if 'snow' key exists in the response
        if 'snow' in data:
            snowfall = data['snow'].get('1h', 0)  # Get snowfall in the last hour (if available), default to 0 if not available
        else:
            snowfall = 0
        return weather_description, temperature_celsius, humidity, rainfall, snowfall
    else:
        return None, None, None, None, None

def main():
    st.title("Real-Time Weather App")
    st.write("Enter the latitude and longitude to get real-time weather data.")

    latitude = st.number_input("Latitude", value=35.7796, step=0.0001)
    longitude = st.number_input("Longitude", value=-78.6382, step=0.0001)
    api_key = st.text_input("OpenWeatherMap API Key")

    if st.button("Get Weather Data"):
        location = get_location(latitude, longitude)
        if location:
            st.write(f"Location: {location}")
            weather_description, temperature, humidity, rainfall, snowfall = get_weather_data(latitude, longitude, api_key)
            if weather_description is not None:
                html_content = f"""
                <h3>Weather Information</h3>
                <p><strong>Location:</strong> {location}</p>
                <p><strong>Weather:</strong> {weather_description}</p>
                <p><strong>Temperature:</strong> {temperature:.2f} °C</p>
                <p><strong>Humidity:</strong> {humidity}%</p>
                <p><strong>Rainfall:</strong> {rainfall} mm</p>
                <p><strong>Snowfall:</strong> {snowfall} mm</p>
                """
                st.markdown(html_content, unsafe_allow_html=True)
            else:
                st.error("Failed to fetch weather data. Please check your latitude, longitude, and API key.")
        else:
            st.error("Failed to fetch location information. Please check your latitude and longitude.")

if __name__ == "__main__":
    main()
