import requests

def get_weather(city, api_key):
    """Fetch and display weather details for a given city."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}

        response = requests.get(url, params=params)
        response.raise_for_status()  # raises error for bad responses

        data = response.json()

        print("\n🌤 WEATHER REPORT 🌤")
        print(f"🏙 City: {data['name']}, {data['sys']['country']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁️  Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError:
        print("⚠️ Invalid city name or API key.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except KeyError:
        print("⚠️ Unexpected response format from API.")

def main():
    print("=== 🌍 Simple Weather App ===")
    API_KEY = "your_openweather_api_key"  # Replace with your actual API key
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city, API_KEY)
    else:
        print("⚠️ Please enter a valid city name.")

if __name__ == "__main__":
    main()
