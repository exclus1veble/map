from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Карта')],
    [KeyboardButton(text='Добавить событие')]
], resize_keyboard=True, one_time_keyboard=True)