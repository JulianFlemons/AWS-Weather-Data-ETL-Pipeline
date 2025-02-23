import pandas as pd
import json

# Load the extracted data from weather_data.json
with open('weather_data.json', 'r') as file:
    data = json.load(file)

forecast_data = []


#Loop through the list of weather forecasts 
for entry in data['list']:
    date_time = entry['dt_txt']
    temperature = entry['main']['temp']
    humidity = entry['main']['humidity']
    wind_speed = entry['wind']['speed']
    description = entry['weather'][0]['description'].capitalize()

# Add formatted data to the list
    forecast_data.append({
        "Date": pd.to_datetime(date_time).strftime('%m/%d/%Y'),  # Convert date format
        "Time": pd.to_datetime(date_time).strftime('%H:%M:%S'),  # Extract time
        "Temperature (°F)": temperature,
        "Humidity (%)": humidity,
        "Wind Speed (mph)": wind_speed,
        "Weather Description": description
     })   
# Convert the list into a pandas DataFrame
df = pd.DataFrame(forecast_data)

# Save the cleaned and transformed data to a CSV file
df.to_csv('transformed_weather_data.csv', index=False)

print("Weather data transformed and saved as transformed_weather_data.csv!")