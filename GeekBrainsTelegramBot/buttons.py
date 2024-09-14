from pyrogram.types import KeyboardButton
from pyrogram import emoji

# buttons for main_keyboard
time_button = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
settings_button = KeyboardButton(f'{emoji.GEAR} Настройки')
weather_button = KeyboardButton(f'{emoji.SUN} Погода')

# buttons for settings_keyboard
back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
