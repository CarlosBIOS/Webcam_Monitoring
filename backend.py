import requests
from os import getenv
from geopy.geocoders import Nominatim


def get_data(place: str, day: str, kind: str) -> list:
    geolocator = Nominatim(user_agent="meu_aplicativo")
    cidade = place
    localizacao = geolocator.geocode(cidade)
    if localizacao:
        latitude: float= localizacao.latitude
        longitude: float = localizacao.longitude

        parameters = {
            'apikey': getenv('api_key_openweather'),
            'lat': latitude,
            'lon': longitude,
            'units': 'metric',
            'lang': 'pt',
            'cnt': int(day) * 8
        }
        request = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
        request.raise_for_status()
        data: list = request.json()['list']
        if kind == 'Temperature':
            filtered_data: list = [[data_day['main']['temp'] for data_day in data]]
        else:
            filtered_data: list = [[data_day['weather'][0]['main'] for data_day in data]]
        filtered_data += [[data_day['dt_txt'] for data_day in data]]

        return filtered_data
    else:
        print("Localização não encontrada.")
