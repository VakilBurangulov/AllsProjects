from pyrogram.types import KeyboardButton, InlineKeyboardButton
from pyrogram import emoji

# buttons for main_keyboard
time_button = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
settings_button = KeyboardButton(f'{emoji.GEAR} Настройки')
weather_button = KeyboardButton(f'{emoji.SUN} Погода')

# buttons for settings_keyboard
back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

# buttons for inline_keyboard
weather_current_inline_button = InlineKeyboardButton(f'{emoji.FIVE_O_CLOCK} Погода сейчас', 'weather_current')
weather_forecast_inline_button = InlineKeyboardButton(f'{emoji.CALENDAR} Прогноз погоды', 'weather_forecast')
