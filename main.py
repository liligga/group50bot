import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
import logging

from handlers import (
    start,
    other_message,
    picture
)

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher(bot)


async def main():
    start.register_handlers(dp)
    picture.register_handlers(dp)
    other_message.register_handlers(dp)
    # запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
