from aiogram.types import Message
from core.keyboards.inline import get_buttons, get_map
from core.utils.states import Steps
from aiogram.fsm.context import FSMContext
# import requests
import json
# import datetime

geotag = []


async def get_start(message: Message, state: FSMContext):
    await message.answer(f'Добро пожаловать! Рады Вас видеть, снова', reply_markup=get_buttons())
    await state.set_state(Steps.START)


async def get_location(message: Message, state: FSMContext):
    await state.update_data(latitude=message.location.latitude)
    await state.update_data(longitude=message.location.longitude)
    await message.answer(f'Введите описание события:')
    await state.set_state(Steps.LOCATION)


async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    marker = await state.get_data()
    latitude: float = marker.get('latitude')
    longitude: float = marker.get('longitude')
    description: str = marker.get('description')
    await state.set_state(Steps.DESCRIPTION)
    await message.answer(f'Событие успешно добавлено!', reply_markup=get_map())
    await state.clear()
    print(marker)

    # Путь к JSON файлу
    json_file_path = 'handlers/markers.json'

    # Новая строка данных для добавления
    marker = (f'"latitude": {latitude}, "longitude": {longitude}, "description": "{description}"')

    # Открываем и читаем JSON файл
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Преобразуем новую строку в формат JSON и добавляем в данные
    new_data = json.loads(marker)
    data.append(new_data)

    # Записываем обновленные данные обратно в JSON файл
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Новая строка данных успешно добавлена в JSON файл.")


"""
async def get_photo(message: Message):
    await message.answer(f'Фото добавлено.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')





