import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    # Fixed: changed 'request' to 'requests' and 'ultsrl' to 'url'
    r = requests.get(url, params={"name": city, "count": 1}, timeout=5)
    data = r.json()

    # Fixed: moved '== 0' outside of the len() function brackets
    if "results" not in data or len(data["results"]) == 0:
        return None

    place = data["results"][0]  
    return {
        "name": place["name"],
        "country": place["country_code"],
        "lat": place["latitude"],
        "lon": place["longitude"]
    }

# Test it
print(get_coordinates("Dubai"))
print(get_coordinates("New York"))

def get_weather(lat, lon):
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=5
        )
        if r.status_code == 200:
            return r.json()["current_weather"]
        return None
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return None
    
def weather_message(temp):
    if temp >= 35: return "🔥 Very hot — stay hydrated!"
    elif temp >= 25: return "😊 Warm and pleasant"
    elif temp >= 15: return "🌤️ Mild weather"
    else: return "❄️  Cold — dress warm!"

while True:
    city = input("\nEnter city (or 'quit'): ").strip()
    if city.lower() == "quit":
        print("Goodbye!")
        breakDubai

    location = get_coordinates(city)
    if not location:
        print(f"City '{city}' not found. Try again.")
        continue

    weather = get_weather(location["lat"], location["lon"])
    if weather:
        print(f"\n📍 {location['name']}, {location['country']}")
        print(f"🌡️  Temperature : {weather['temperature']}°C")
        print(f"💨 Wind speed  : {weather['windspeed']} km/h")
        print(weather_message(weather["temperature"]))