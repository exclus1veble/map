from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_buttons():
     keyboard_builder = InlineKeyboardBuilder()
     keyboard_builder.button(text='Открыть карту 🗺', url='https://t.me/survival_map_bot/map')
     keyboard_builder.button(text='Добавить событие', callback_data='add_ivent')

     keyboard_builder.adjust(1)
     return keyboard_builder.as_markup()

def get_map():
     keyboard_builder = InlineKeyboardBuilder()
     keyboard_builder.button(text='Открыть карту 🗺', url='https://t.me/survival_map_bot/map')

     keyboard_builder.adjust(2)
     return keyboard_builder.as_markup()