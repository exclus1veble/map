from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from core.keyboards.inline import get_buttons, get_map
from core.keyboards.reply import reply_keyboard
from aiogram.fsm.context import FSMContext
import requests
import json
import datetime


async def get_start(message: Message, bot: Bot):
        await message.answer('Добро пожаловать! Мы помогаем Вам спасать самих себя',
                         reply_markup=get_buttons())

# Cписок добавленных локаций
locations = []

# Создание словаря локации
location = {
    "latitude": None,
    "longitude": None,
    "description": None,
    "photo": None     # фото не запрашивается, но если оправят, то оно добавиться к текущему событию
            }

async def get_location(message: Message, bot: Bot):
    location['latitude'] = {message.location.latitude}
    location['longitude'] = {message.location.longitude}
    await message.answer(f'Введите описание события:')




async def get_description(message: Message):
    location["description"] = (message.text)
    locations.append(location)
    print(location)
    await message.answer(f'Событие успешно добавлено на карту!', reply_markup=get_map())

    # async def get_photo(message: Message, bot: Bot):
    #    await message.answer(f'Фото добавлено.')
    #    file = await bot.get_file(message.photo[-1].file_id)
    #    await bot.download_file(file.file_path, 'photo.jpg')