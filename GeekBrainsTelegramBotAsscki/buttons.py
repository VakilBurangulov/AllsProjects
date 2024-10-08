from pyrogram.types import KeyboardButton
from pyrogram import emoji

# buttons for ascii_keyboard
happy_button = KeyboardButton(f'{emoji.SMILING_FACE} Весёлые')
hello_button = KeyboardButton(f'{emoji.RAISED_HAND} Приветствие')
sad_button = KeyboardButton(f'{emoji.CRYING_FACE}  Грустные')
angry_button = KeyboardButton(f'{emoji.ENRAGED_FACE} Злость')


# buttons for cat_keyboard
cat_button = KeyboardButton(f'{emoji.CAT_FACE} Рандомный котик')


# buttons for settings_keyboard
cats_button = KeyboardButton(f'{emoji.CAT} Коты')
ascii_button = KeyboardButton(f'{emoji.SMILING_FACE} ASCII')
help_button = KeyboardButton(f'{emoji.LINK} Помощь')
back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

