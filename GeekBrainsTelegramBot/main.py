# import packages inside python
import datetime
import time
import operator

# import downloaded packages
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, ForceReply

# import my local files
import config  # secret file
import buttons
import keyboards
from custom_filters import button_filter, inline_button_filter, reply_text_filter
from weather import get_current_weather, get_forecast
from database import Database


class Client(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database = Database()
        
    def stop(self, *args, **kwargs):
        self.database.close()
        return super().stop(*args, **kwargs)


bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name='VakilBot'
)


@bot.on_message(filters=filters.command("start"))
async def start_command(bot: Client, message: Message):
    user = bot.database.get_user(message.from_user.id)
    if user is None:
        bot.database.create_user(message.from_user.id)
    await message.reply(f'Привет, {message.from_user.username}', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("calc"))
async def calc_command(bot: Client, message: Message):
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
async def time_command(bot: Client, message: Message):
    timezone = (time.timezone/3600)/-1
    timezone_sign = '+' if timezone > 0 else ''
    timezone = f'{timezone_sign}{timezone}'
    current_time = time.strftime("%H:%M:%S")
    await message.reply(f'Привет текущее время, {current_time}\nВаш часовой пояс {timezone}', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=button_filter(buttons.settings_button))
async def settings_command(bot: Client, message: Message):
    await message.reply('Переход в настройки', reply_markup=keyboards.settings_keyboard)


@bot.on_message(filters=button_filter(buttons.back_button))
async def back_command(bot: Client, message: Message):
    await message.reply('Возврат в главное менюю', reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("help") | button_filter(buttons.help_button))
async def help_command(bot: Client, message: Message):
    await message.reply(f"""Привет вот список существующих команд
    \n /start-Запускает бота\n /time - Показывает время в онлайн\n /calc - Калькулятор\n /weather - Показывает погоду в твоём городе""", reply_markup=keyboards.main_keyboard)


@bot.on_message(filters=filters.command("weather") | button_filter(buttons.weather_button))
async def weather_command(bot: Client, message: Message):
    user = bot.database.get_user(message.from_user.id)
    if user is not None and user.city is not None:
        city = user.city
    else:
        city = 'Москва'
        await message.reply(f'Стоит стандартный город {city}.\nЕсли хотите изменить город перейдите в настройки')
    await message.reply(get_current_weather(city), reply_markup=keyboards.weather_inline_keyboard)


@bot.on_callback_query(filters=inline_button_filter(buttons.weather_current_inline_button))
async def weather_current_callback(bot: Client, query: CallbackQuery):
    user = bot.database.get_user(query.from_user.id)
    if user is not None and user.city is not None:
        city = user.city
    else:
        city = 'Москва'
    weather = get_current_weather(city)
    if weather == query.message.text:
        return
    await query.message.edit_text(weather, reply_markup=keyboards.weather_inline_keyboard)


@bot.on_callback_query(filters=inline_button_filter(buttons.weather_forecast_inline_button))
async def weather_forecast_callback(bot: Client, query: CallbackQuery):
    user = bot.database.get_user(query.from_user.id)
    if user is not None and user.city is not None:
        city = user.city
    else:
        city = 'Москва'
    weather = get_forecast(city)
    if weather == query.message.text:
        return
    await query.message.edit_text(weather, reply_markup=keyboards.weather_inline_keyboard)

change_city_text = 'Меняем город, напиши в ответном сообщении город, который хочешь сохранить'


@bot.on_message(filters=button_filter(buttons.change_city_button))
async def change_city_command(bot: Client, message: Message):
    await bot.send_message(message.chat.id, change_city_text, reply_markup=ForceReply(True))


@bot.on_message(filters=filters.reply & reply_text_filter(change_city_text))
async def change_city_reply(bot: Client, message: Message):
    city = message.text
    bot.database.set_city(message.from_user.id, city)
    await message.reply('Город успешно изменен', reply_markup=keyboards.main_keyboard)


@bot.on_message()
async def echo_command(bot: Client, message: Message):
    await message.reply(message.text)

if __name__ == "__main__":
    bot.run()
