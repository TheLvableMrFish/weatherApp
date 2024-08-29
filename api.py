import requests

def get_coordinates(city_name):
    geocode_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json"
    response = requests.get(geocode_url, headers="")
    data = response.json()
    if(data):
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None, None
    
def get_current_weather(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(weather_url, headers="")
    data = response.json()

    return data

def get_weeks_weather(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America/New_York"
    response = requests.get(weather_url, headers="")
    data = response.json()

    return data


def get_dates(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America/New_York"
    response = requests.get(weather_url, headers="")
    data = response.json()
    
    return data