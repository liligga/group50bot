import asyncio
import logging

from bot_config import dp
from handlers import start, picture, other_message, complaint_dialog


async def main():
    start.register_handlers(dp)
    picture.register_handlers(dp)
    complaint_dialog.register_handlers(dp)

    # обязательно в самом конце
    other_message.register_handlers(dp)
    # запуск бота
    await dp.start_polling()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
