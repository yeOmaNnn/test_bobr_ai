class ShowWeatherService:
    def __init__(self, weather_api):
        self.weather_api = weather_api

    def get_weather(self, city: str):
        data = self.weather_api.get_weather_data(city)
        if "error" in data:
            return data['error']

        if data:
            description = data['weather'][0]["description"]
            temp = data['main']["temp"]
            wind_speed = data['wind']["speed"]
            return ("Погода в {}: \n Температура: {}°C \n Скорость ветра: {} м/с \n Описание: {}".format(city, temp, wind_speed, description))

        else:
            return "Данные о погоде не удалось получить"
