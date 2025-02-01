import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message):
    user = message.from_user
    # user.first_name
    # user.last_name
    # user.username
    # user.id
    await message.answer(f"Hello, {user.first_name}")


@dp.message_handler()
async def echo_handler(message):
    text = message.text
    await message.answer(text)


async def main():
    # запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
