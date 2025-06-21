import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual OpenWeatherMap API key
API_KEY = "b3f716d26c43a49a4529045bb6876026"

# Cities to get weather data for
cities = ["Chennai", "Mumbai", "Delhi", "Kolkata", "Bangalore"]

# Base API URL
URL = "http://api.openweathermap.org/data/2.5/weather"

# Create dictionary to store data
weather_data = {
    "City": [],
    "Temperature (°C)": [],
    "Humidity (%)": [],
    "Pressure (hPa)": []
}

# Fetch weather data for each city
for city in cities:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data["City"].append(city)
        weather_data["Temperature (°C)"].append(data["main"]["temp"])
        weather_data["Humidity (%)"].append(data["main"]["humidity"])
        weather_data["Pressure (hPa)"].append(data["main"]["pressure"])
    else:
        print(f"Failed to get data for {city}: {data.get('message')}")

# Create graph
sns.set(style="whitegrid")
fig, axes = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle("Current Weather Data", fontsize=16)

sns.barplot(x=weather_data["City"], y=weather_data["Temperature (°C)"], ax=axes[0], palette="coolwarm")
axes[0].set_title("Temperature (°C)")

sns.barplot(x=weather_data["City"], y=weather_data["Humidity (%)"], ax=axes[1], palette="Blues")
axes[1].set_title("Humidity (%)")

sns.barplot(x=weather_data["City"], y=weather_data["Pressure (hPa)"], ax=axes[2], palette="Greens")
axes[2].set_title("Pressure (hPa)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
