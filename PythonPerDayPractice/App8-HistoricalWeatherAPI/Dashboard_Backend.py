import requests
import os
import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')

API_KEY = os.environ.get("WEATHER-API")

def get_data(place, forecast_days = None):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

        response = requests.get(url)
        data = response.json()

        filtered_data = data["list"]
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]

        return filtered_data
    except KeyError as e:
        return None

if __name__ == "__main__":
    print(get_data("Noida", forecast_days=2))
    pass