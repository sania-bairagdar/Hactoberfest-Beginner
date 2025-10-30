import requests

API_KEY = "your_openweather_api_key"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

res = requests.get(url)
if res.status_code == 200:
    data = res.json()
    print(f"🌤 City: {data['name']}")
    print(f"🌡 Temperature: {data['main']['temp']}°C")
    print(f"💨 Wind: {data['wind']['speed']} m/s")
else:
    print("City not found or invalid API key.")
