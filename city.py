import requests


class City:
    def __init__(self,
                 name: str,
                 latitude: float,
                 longitude: float):
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude

        self.__get_temperatures()

    def show(self):
        print(self.__name)
        print('Temperatura actual: ')

    def __get_temperatures(self):
        response = requests.get(
            url='https://api.open-meteo.com/v1/forecast',
            params={
                "latitude": self.__latitude,
                "longitude": self.__longitude,
                "hourly": "temperature_2m",
                "forecast_days": 1
            }
        ).json()
        print(response)
