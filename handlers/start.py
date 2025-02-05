from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# @dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    user = message.from_user
    # user.first_name - имя пользователя, есть всегда
    # user.last_name - фамилия, может не быть
    # user.username - ник пользователя(@), может не быть
    # user.id - уникальный индетификатор пользователя, есть всегда, в виде чмсла
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
            InlineKeyboardButton(text="Наш инстаграм", url="https://geeks.kg"),
        ],
        [
            InlineKeyboardButton(text="О нас", callback_data="aboutus"),
        ]
    ])
    await message.answer(f"Приветствуем вас, {user.first_name}", reply_markup=kb)


async def about_us_handler(callback: CallbackQuery):
    # await callback.answer("О нас", show_alert=True)
    await callback.message.answer("О нас")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_callback_query_handler(about_us_handler, lambda c: c.data == "aboutus")
