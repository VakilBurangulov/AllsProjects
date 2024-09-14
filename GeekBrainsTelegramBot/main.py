# import packages inside python
import time
import operator

# import downloaded packages
from pyrogram import Client, filters
from pyrogram.types import Message

# import my local files
import config  # secret file
import buttons
import keyboards
from custom_filters import button_filter
from weather import get_current_weather

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name='VakilBot'
)


@bot.on_message(filters=filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply(f'Привет, {message.from_user.username}', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("calc"))
async def calc_command(client: Client, message: Message):
    math_operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    if len(message.command) != 4:
        return await message.reply('Неверное кол-во аргументов, пример команды /calc 10 - 2')
    _, n1, op, n2 = message.command
    op = math_operators.get(op)
    if op is None:
        return await message.reply('Неизвестный оператор')
    if not n1.isdigit() or not n2.isdigit():
        return await message.reply("Аргументы должны быть числами")
    await message.reply(f'Результат: {op(int(n1), int(n2))}')


@bot.on_message(filters=filters.command("time") | button_filter(buttons.time_button))
async def time_command(client: Client, message: Message):
    current_time = time.strftime("%H:%M:%S")
    await message.reply(f'Привет текущее время, {current_time}', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=button_filter(buttons.settings_button))
async def settings_command(client: Client, message: Message):
    await message.reply('Переход в настройки пока что здесь пусто', reply_markup=keyboards.settings_keyboard)


@bot.on_message(filters=button_filter(buttons.back_button))
async def back_command(client: Client, message: Message):
    await message.reply('Возврат в главное менюю', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("help") | button_filter(buttons.help_button))
async def help_command(client: Client, message: Message):
    print('help')
    await message.reply(f"""Привет вот список существующих команд
    \n /start-Запускает бота\n /time - Показывает время в онлайн\n /calc - Калькулятор\n /weather - Показывает погоду в твоём городе""", reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("weather") | button_filter(buttons.weather_button))
async def weather_command(client: Client, message: Message):
    city = 'Домодедово'
    await message.reply(get_current_weather(city))


@bot.on_message()
async def echo_command(client: Client, message: Message):
    await message.reply(message.text)

bot.run()
