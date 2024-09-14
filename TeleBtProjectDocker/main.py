import telebot
import os
import random
from telebot import types

token = '5993234240:AAHEqBrRMds1oP-JcdsYgCrQ24tSW4bdnu4'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['tag'])
def add_id(message):
        username = str(message.from_user.username) # Записываем в переменую username тег адресанта
        id = str(message.from_user.id) # Записываем в переменую id идентификатор адресанта
        file = open(('tags/'+username+'.txt'), 'w+')
        file.write(id)
        file.close()
        if message.from_user.language_code == 'ru':
            bot.send_message(message.from_user.id, 'Ваш тег записан')
        else:
            bot.send_message(message.from_user.id, 'Your tag is recorded')
@bot.message_handler(commands=['start'])
def send_text(message):
    print(message.from_user.language_code)
    if message.from_user.language_code == 'ru':
        bot.send_message(message.chat.id, 'Привет если ты хочешь отправить открытку то пожалуйста отправь сюда тег зарегистрированова адресата без @ которому хочешь отправить открытку. Например: Vany_Ivanov\nИли напиши /tag что бы зарегистрироваться и тебе могли отправлять открытки')
    else:
        bot.send_message(message.chat.id,'Hi, if you want to send a postcard, then please send here the tag of the registered  without @ to whom you want to send a postcard. For example: Vany_Ivanov\n Or write /tag to write down your tag and they could send you valentines')
# @bot.message_handler()
# def send_valentin(message):
#     folder = './tags'
#     fil = (message.text+'.txt')
#     path = os.path.join(folder, fil)
#     if os.path.isfile(path):
#          with  open(('tags/'+message.text+'.txt'),'r') as file:
#             id = file.read()
#          num = str(random.randint(1, 5))
#          markup = types.InlineKeyboardMarkup(row_width=1)
#          if message.from_user.language_code == 'ru':
#             button1 = types.InlineKeyboardButton('Да', callback_data='Yes')
#             button2 = types.InlineKeyboardButton('Нет', callback_data='No')
#          else:
#             button1 = types.InlineKeyboardButton('Yes', callback_data='Yes')
#             button2 = types.InlineKeyboardButton('No', callback_data='No')
#
#          markup.add(button1, button2)
#
#          if message.from_user.language_code == 'ru':
#             mes = bot.send_message(message.chat.id, 'Ты хочешь что бы адресат увидел что открытка пришла от тебя?', reply_markup=markup)
#          else:
#             mes = bot.send_message(message.chat.id, 'Do you want the recipient to see that the valentine came from you?', reply_markup=markup)
#
#          @bot.callback_query_handler(func=lambda call: True)
#          def callback(call):
#                 if call.message:
#                     if call.data == 'Yes':
#                         bot.send_message(int(id), text=f'Вам пришла открытка от {message.from_user.username}')
#                         with open('img/' + num + '.jpg', 'rb') as img:
#                             bot.send_photo(int(id), img)
#                     elif call.data == 'No':
#                         with open('img/' + num + '.jpg', 'rb') as img:
#                             bot.send_photo(int(id), img)
#                     try:
#                         bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)
#
#                     except Exception as ex:
#                         print(ex)
#
#
#                 if message.from_user.language_code == 'ru':
#                     bot.send_message(message.chat.id, 'Валентинка отправлена')
#                 else:
#                     bot.send_message(message.chat.id, 'The Valentine card has been sent')
#
#
#     else:
#         if message.from_user.language_code == 'ru':
#             bot.send_message(message.chat.id, 'Я тебя не понимаю')
#         else:
#             bot.send_message(message.chat.id, 'I dont understand you')

@bot.callback_query_handler(func= lambda call: True)
def call_back(call):
            if call.message:
                num = random.randint(1, 10)
                if call.data == 'Yes':
                    bot.send_message(int(id), text=f'Вам пришла открытка от {mes.from_user.username}')
                    bot.send_photo(int(id), open('img/' + str(num) + '.jpg', 'rb'))

                elif call.data == 'No':
                    bot.send_photo(int(id), open('img/' + str(num) + '.jpg', 'rb'))
                    if mes.from_user.language_code == 'ru':
                                    bot.send_message(mes.chat.id, 'Открытка отправлена')
                    else:
                                    bot.send_message(mes.chat.id, 'The postcard has been sent')
                bot.delete_message(chat_id=mes.chat.id, message_id=m.message_id)


@bot.message_handler()
def send_valentin(message):

    folder = './tags'
    fil = (message.text+'.txt')
    path = os.path.join(folder, fil)
    if os.path.isfile(path):
        global mes
        mes = message
        global id
        with open(('tags/'+message.text+'.txt'), 'r') as f:
            id = f.read()
        markup = types.InlineKeyboardMarkup(row_width=1)

        if message.from_user.language_code == 'ru':
                    button1 = types.InlineKeyboardButton('Да', callback_data='Yes')
                    button2 = types.InlineKeyboardButton('Нет', callback_data='No')
        else:
                    button1 = types.InlineKeyboardButton('Yes', callback_data='Yes')
                    button2 = types.InlineKeyboardButton('No', callback_data='No')

        markup.add(button1, button2)

        global m
        if message.from_user.language_code == 'ru':
            m = bot.send_message(message.chat.id, 'Ты хочешь что бы адресат увидел что открытка пришла от тебя?', reply_markup=markup)
        else:
            m = bot.send_message(message.chat.id, 'Do you want the recipient to see that the postcard came from you?', reply_markup=markup)


    else:
        if message.from_user.language_code == 'ru':
            bot.send_message(message.chat.id, 'Я тебя не понимаю')
        else:
            bot.send_message(message.chat.id, 'I dont understand you')

bot.polling()
