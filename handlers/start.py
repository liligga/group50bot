from aiogram import Dispatcher, types


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user = message.from_user
    # user.first_name - имя пользователя, есть всегда
    # user.last_name - фамилия, может не быть
    # user.username - ник пользователя(@), может не быть
    # user.id - уникальный индетификатор пользователя, есть всегда, в виде чмсла
    await message.answer(f"Hello, {user.first_name}")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
