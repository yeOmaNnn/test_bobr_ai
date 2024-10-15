import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram import Router
from aiogram.filters import Command

from app.core.config import API_TOKEN, WEATHER_API_TOKEN
from app.repositories.repositories import GetWeather
from app.service.service import ShowWeatherService

API_TOKEN = API_TOKEN
WEATHER_API_TOKEN = WEATHER_API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

router = Router()

weather_api = GetWeather(WEATHER_API_TOKEN)
weather_service = ShowWeatherService(weather_api)


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет, я погодный бот! Отправь мне название города, а я пришлю тебе краткую сводку погоды!")


@router.message()
async def get_weather(message: types.Message):
    city = message.text
    weather_info = weather_service.get_weather(city)
    await message.reply(weather_info)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
