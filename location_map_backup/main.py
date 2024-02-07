import betterlogging as logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.handlers.basic import get_start, get_location, get_description#, get_photo
from core.handlers.callback import select_button
from core.settings import settings
import asyncio


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот остановлен!")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_location, F.location)
    #dp.message.register(get_photo, F.photo)
    dp.callback_query.register(select_button, F.data.startswith("add"))
    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_description, F.text)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
