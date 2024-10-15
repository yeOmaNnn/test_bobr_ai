import requests


class GetWeather:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city: str):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru",
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "Превышено время ожидания ответа от сервера."}
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                return {"error": f"Город '{city}' не найден. Проверьте правильность написания."}
            return {"error": f"HTTP ошибка: {http_err}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Ошибка при выполнении запроса: {e}"}
