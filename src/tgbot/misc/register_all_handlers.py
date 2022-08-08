from aiogram import Dispatcher

from tgbot.handlers.users import register_user
from tgbot.misc.set_bot_commands import set_default_commands


async def register_all_handlers(dp: Dispatcher):
    """
    This function registers everything handlers
    """
    register_user(dp)

    await set_default_commands(dp)
