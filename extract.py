import requests
import json
from dotenv import load_dotenv
import os
#Load environment variables from .env file 


api_key = os.getenv("OPENWEATHER_API_KEY")

city = "Washington D.C."

# Define the API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial"

# Send the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Save the response data to a JSON file
    with open('weather_data.json', 'w') as file:
        json.dump(data, file, indent=4)

    print(" Weather data extracted and saved to weather_data.json!")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
