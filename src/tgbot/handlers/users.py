from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import start_keyboard


async def start(message: Message):
    """
    This function sends an inline keyboard after the start command
    """
    keyboard = start_keyboard()
    await message.answer('Информация', reply_markup=keyboard)
    await message.bot.delete_message(message.chat.id, message.message_id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(
        start, commands=['start'], state="*"
    )
