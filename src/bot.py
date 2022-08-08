import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.settings.const import TOKEN

from tgbot.misc.register_all_handlers import register_all_handlers


async def main():
    storage = MemoryStorage()

    bot = Bot(TOKEN)
    dp = Dispatcher(bot, storage=storage)

    await register_all_handlers(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
