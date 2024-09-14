import telebot
import sqlite3

bot = telebot.TeleBot(token='5993234240:AAHEqBrRMds1oP-JcdsYgCrQ24tSW4bdnu4')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, tag TEXT)")
    conn.commit()
    cur.execute("SELECT * FROM users WHERE id = ?", (message.chat.id,))
    res = cur.fetchone()
    conn.close()
    if res is None:
        bot.send_message(message.chat.id, 'Привет, ты ещё не зарегистрирован напиши /tag и я тебя зарегистрирую')
        bot.register_next_step_handler(message, tag)
    else:
        bot.send_message(message.chat.id,
                         """Привет, ты уже зарегистрирован поэтому ты можешь отправить кому-нибудь открытку.\nДля этого тебе нужно написать Тег адресанта без @.\nТак же ты можешь написать подпись к открытке через слэш.\nПример: Vany_Ivanov/Привет поздравляю""")
        bot.register_next_step_handler(message, send_photo)


def send_photo(message):

    mes = message.text.strip().split('/')
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE tag = ?", (mes[0],))
    res = cur.fetchone()
    conn.close()

    if res is None:
        bot.send_message(message.chat.id, 'Я не знаю такого пользователя, попробуй снова')
        bot.register_next_step_handler(message, send_photo)
    else:
        if len(mes) == 1:
            with open('img/image.jpg', 'rb') as f:
                bot.send_photo(res[0], f)
            bot.send_message(message.chat.id, 'Фото отправлено, можете написать следующего человека')
            bot.register_next_step_handler(message, send_photo)
        elif len(mes) == 2:
            with open('img/image.jpg', 'rb') as f:
                bot.send_photo(res[0], f, caption=mes[1])
                bot.send_message(message.chat.id, 'Фото отправлено, можете написать следующего человека')
                bot.register_next_step_handler(message, send_photo)


def tag(message):
    if message.text == '/tag':
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES (?, ?)", (message.chat.id, message.from_user.username))
        conn.commit()

        conn.close()
        bot.send_message(message.chat.id, 'Ты зарегистрирован')
        bot.send_message(1613568957, f'Новый пользователь id:{message.chat.id}, username:{message.from_user.username}')
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял попробуй написать /tag еще раз')
        bot.register_next_step_handler(message, tag)


bot.polling(none_stop=True)
