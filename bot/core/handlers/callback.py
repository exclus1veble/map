from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_button(call: CallbackQuery, bot: Bot):
    button = call.data.split('_')[0]
    answer = f'Отправьте геолокацию события, для добавления его на карту города. На устройстве геолокацию включать НЕ обязательно!'

    await call.message.answer(answer)
    await call.answer()
