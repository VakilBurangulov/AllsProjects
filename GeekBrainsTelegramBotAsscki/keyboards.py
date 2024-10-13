# import downloaded packages
from pyrogram.types import ReplyKeyboardMarkup

# import my local files
import buttons

cat_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.cat_button, buttons.back_button],
    ],
    resize_keyboard=True
)

ascii_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.happy_button, buttons.hello_button],
        [buttons.sad_button, buttons.angry_button],
        [buttons.back_button]
    ],
    resize_keyboard=True
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.ascii_button, buttons.cats_button],
        [buttons.help_button]
    ],
    resize_keyboard=True
)
