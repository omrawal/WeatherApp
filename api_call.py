# mapbox
import requests
from urllib.parse import quote

# returns the coordinates of the place


def getCoordinates(place):
    place = place.replace(' ', '%20')
    api_link = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1Ijoib20tcmF3YWwiLCJhIjoiY2tvcXd5OWlvMHo5cTJwc2pnNm5zdmc1eiJ9.9rBCyMoTb7TgWpsSQahwkA".format(
        place)
    api_get = requests.get(api_link)
    api_get_json = api_get.json()
    place_name, long, lat = api_get_json['features'][0]['place_name'], api_get_json['features'][0][
        'geometry']['coordinates'][0], api_get_json['features'][0]['geometry']['coordinates'][1]
    return (place_name, long, lat)


# climacell

def getLiveWeather(lat, long, place_name):
    url = "https://api.climacell.co/v3/weather/realtime"

    querystring = {"lat": lat, "lon": long, "unit_system": "si", "fields": [
        "temp", "feels_like", "humidity", "wind_speed", "precipitation", "precipitation_type", "weather_code"], "apikey": "nZBN8tA17HfWZgCiRx56lUrRXBiD04tG"}

    headers = {"Accept": "application/json"}

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    response = response.json()
    ans = {}
    ans['Place'] = place_name
    ans['Actual_Temp'] = '{} C'.format(response['temp']['value'])
    ans['Feels like'] = '{} C'.format(response['feels_like']['value'])
    ans['Windspeed'] = '{} m/s'.format(response['wind_speed']['value'])
    ans['Humidity'] = '{} %'.format(response['humidity']['value'])
    ans['Precipitation'] = '{} mm/hr'.format(
        response['precipitation']['value'])
    ans['Precipitation_Type'] = response['precipitation_type']['value']
    ans['Weather_Code'] = response['weather_code']
    return ans


def getLiveWeatherOf(place):
    place_name, long, lat = getCoordinates(place=place)
    return getLiveWeather(lat=lat, long=long, place_name=place_name)
