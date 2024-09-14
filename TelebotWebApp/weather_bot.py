import requests
import telebot
from telebot import types

bot = telebot.TeleBot('7200366460:AAFmQH_8Y_k7hCjJw3rvYLMcrwT6BbU1XJQ')
API = '824e44a012cc4edfe3f5fc4f9cd0d3eb'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет напиши название города на английском, а я скажу какая сейчас в этом городе погода')
    bot.register_next_step_handler(message, get_temp)


def get_temp(message):
    try:
        city = message.text.lower().strip()
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        bot.send_message(message.chat.id, f'Погода в этом городе: {temp}°C, напишите следующий город')
        bot.register_next_step_handler(message, get_temp)
    except KeyError:
        bot.send_message(message.chat.id, 'Я не знаю такого города, попробуйте написать название другого города')
        bot.register_next_step_handler(message, get_temp)


bot.polling(none_stop=True)
