from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


# FSM - finite state machine
class Complaint(StatesGroup):
    name = State()
    age = State()
    text = State()


async def start_dialog(callback: CallbackQuery):
    await Complaint.name.set()
    await callback.message.answer("Как вас зовут")


async def process_name(message: Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data["name"] = name
    await Complaint.next()
    await message.answer("Сколько Вам лет")


async def process_age(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
    await Complaint.next()
    await message.answer("Какая у вас жалоба?")


async def process_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text
    await state.finish()
    await message.answer("Спасибо за отзыв.")


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == "complaint")
    dp.register_message_handler(process_name, state=Complaint.name)
    dp.register_message_handler(process_age, state=Complaint.age)
    dp.register_message_handler(process_text, state=Complaint.text)
