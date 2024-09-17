from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.time_button, buttons.help_button, buttons.weather_button],
        [buttons.settings_button]
    ],
    resize_keyboard=True
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.back_button],
    ],
    resize_keyboard=True
)

weather_inline_keyboard = InlineKeyboardMarkup(
    [
        [buttons.weather_current_inline_button],
        [buttons.weather_forecast_inline_button]
    ]
)
