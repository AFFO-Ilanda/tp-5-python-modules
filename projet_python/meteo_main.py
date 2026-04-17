import requests

API_KEY = "OpenWeatherMap"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
VILLE = "Dakar"

params = {
    "q": VILLE,
    "appid": API_KEY,
    "units": "metric",
    "lang": "fr"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidite = data["main"]["humidity"]

    print(f"Météo à {VILLE} :")
    print(f" -- Température : {temperature} ℃")
    print(f" -- Description : {description}")
    print(f" -- Humidité : {humidite}%")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
    print(response.text)
