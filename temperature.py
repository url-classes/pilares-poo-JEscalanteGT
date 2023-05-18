import datetime


class Temperature:
    def __init__(self,
                 measure: float,
                 created_at: datetime):
        self.__measure = measure
        self.__created_at = created_at
        self.__unit = '°C'

    def __str__(self) -> str:
        return f'' \
               f'Temperatura: {self.__measure}' \
               f'{self.__unit}, ' \
               f'Hora: {self.__created_at}'
