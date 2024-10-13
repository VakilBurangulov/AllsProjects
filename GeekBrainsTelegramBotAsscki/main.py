# import packages inside python
import random

# import downloaded packages
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, ForceReply
import requests
from requests import Response

# import my local files
import config  # secret file
import buttons
import keyboards
import custom_filters
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
    name='VakilBotASCII'
)


@bot.on_message(filters=filters.command("start"))
async def start_command(bot: Client, message: Message):
    await message.reply(f"Привет {message.from_user.first_name}, я Бот который знает много прикольных ASCII-эмоций", reply_markup=keyboards.settings_keyboard)


@bot.on_message(filters=filters.command("help") | custom_filters.button_filter(buttons.help_button))
async def help_command(bot: Client, message: Message):
    await message.reply("""start - Приветствие рассказ о функциях бота
sad - Отправка рандомного грустного ASCII-эмоджи
angry - Отправка рандомного злого ASCII-эмоджи
happy - Отправка рандомного веселого ASCII-эмоджи
hello - Отправка рандомного приветствующего ASCII-эмоджи
translate_en_ru - Перевод с английского на русский
translate_ru_en - Перевод с русского на английский
cat - Отправляет рандомную фотку кота
help - Помощь""", reply_markup=keyboards.settings_keyboard)


@bot.on_message(filters=custom_filters.button_filter(buttons.cats_button))
async def cats_command(bot: Client, message: Message):
    await message.reply(f'Хорошо перехожу на страницу котиков', reply_markup=keyboards.cat_keyboard)


@bot.on_message(filters=custom_filters.button_filter(buttons.ascii_button))
async def ascii_command(bot: Client, message: Message):
    await message.reply(f'Хорошо перехожу на страницу ascii', reply_markup=keyboards.ascii_keyboard)


@bot.on_message(filters=custom_filters.button_filter(buttons.back_button))
async def back_command(bot: Client, message: Message):
    await message.reply(f'Хорошо перехожу на главную страницу', reply_markup=keyboards.settings_keyboard)


@bot.on_message(filters=filters.command("sad") | custom_filters.button_filter(buttons.sad_button))
async def sad_command(bot: Client, message: Message):
    emoji = ["( ˘︹˘ )", "＞﹏＜", "≡(▔﹏▔)≡",
             "ಥ_ಥ", "(；′⌒`)", "(￣ ‘i ￣;)",
             "/(ㄒoㄒ)/~~", "இ௰இ", "o(TヘTo)"]
    text = random.choice(emoji)
    await message.reply(f"{text}", reply_markup=keyboards.ascii_keyboard)


@bot.on_message(filters=filters.command("angry") | custom_filters.button_filter(buttons.angry_button))
async def angry_command(bot: Client, message: Message):
    emoji = ["╰（‵□′）╯", "(╬▔皿▔)╯)", "(►__◄)",
             "(ง'̀-'́)ง", "╭∩╮( •̀_•́ )╭∩╮", "(｡ •̀ ᴖ •́ ｡ )",
             "(｡•ˇ‸ˇ•｡)", "(╯'□')╯︵ ┻━┻", "(* ￣︿￣))"]
    text = random.choice(emoji)
    await message.reply(f"{text}", reply_markup=keyboards.ascii_keyboard)


@bot.on_message(filters=filters.command("happy") | custom_filters.button_filter(buttons.happy_button))
async def happy_command(bot: Client, message: Message):
    emoji = ["٩(^ᗜ^ )و ´-", "✺◟(＾∇＾)◞✺", "◝(ᵔᵕᵔ)◜",
             "(❁´◡`❁))", "( $ _ $ )", "φ(゜▽゜*)♪",
             "<(˶ᵔᵕᵔ˶)>", "（￣︶￣）↗　", "O(∩_∩)O"]
    text = random.choice(emoji)
    await message.reply(f"{text}", reply_markup=keyboards.ascii_keyboard)


@bot.on_message(filters=filters.command("hello") | custom_filters.button_filter(buttons.hello_button))
async def hello_command(bot: Client, message: Message):
    emoji = ["ヾ(•ω•`)o", "(｡･∀･)ﾉﾞ)", "||ヽ(*￣▽￣*)ノミ|Ю",
             "ヽ(✿ﾟ▽ﾟ)ノ", "( ﾉ ﾟｰﾟ)ﾉ)", "o(*°▽°*)o",
             "✪ ω ✪", "(^^ゞ)", "（づ￣3￣）づ╭❤️～"]
    text = random.choice(emoji)
    await message.reply(f"{text}", reply_markup=keyboards.ascii_keyboard)


def get_random_cat():
    url = "https://cataas.com/cat"
    response = requests.get(f'{url}?json=true')
    cat_id = response.json()["_id"]
    cat_url = f"{url}/{cat_id}"
    return cat_url


def get_translation(text:str, source_lang:str, target_lang: str) -> str | None:
    try_count = 0
    success = False

    def try_get_translation(text, source_lang, target_lang):
        url = "https://translate.redko.us/translate"
        params = {
            "text": text,
            "source_lang": source_lang,
            "target_lang": target_lang
        }
        return requests.get(url, params=params)

    while not success and try_count < 5:
        responce = try_get_translation(text, source_lang, target_lang)
        success = responce.status_code == 200
        try_count += 1

        if success:
            return responce.json()['response']['translated_text']


@bot.on_message(filters=filters.command("translate_en_ru"))
async def translate_en_ru_command(bot: Client, message: Message):
    if len(message.text.split()) == 2:
        text = message.text.split()[1]
        await message.reply(get_translation(text, 'en', 'ru'))
    else:
        await message.reply("Команду нужно вводить вот так /translate_en_ru слово \nПример: /translate_en_ru Car")


@bot.on_message(filters=filters.command("translate_ru_en"))
async def translate_ru_en_command(bot: Client, message: Message):
    if len(message.text.split()) == 2:
        text = message.text.split()[1]
        await message.reply(get_translation(text, 'ru', 'en'))

    else:
        await message.reply("Команду нужно вводить вот так /translate_ru_en слово \nПример: /translate_ru_en Машина")


@bot.on_message(filters=filters.command("cat") | custom_filters.button_filter(buttons.cat_button))
async def cat_command(bot: Client, message:Message):
    await message.reply(get_random_cat())


@bot.on_message()
async def echo(bot: Client, message: Message):
    res = bot.database.get_user(message.from_user.id)
    if res is None:
        await message.reply(f'Привет {message.from_user.first_name}, я не знаю этой команды')
        bot.database.create_user(message.from_user.id)
    elif res.amount == 0:
        await message.reply(f'Привет {message.from_user.first_name}, я не знаю этой команды')
        bot.database.set_amount(message.from_user.id, res.amount+1)
    elif res.amount == 1:
        await message.reply(f'Привет {message.from_user.first_name}, я же сказал что не знаю этой команды')
        bot.database.set_amount(message.from_user.id, res.amount+1)
    elif res.amount == 2:
        await message.reply(f'Меня это реально начинает бесить')
        bot.database.set_amount(message.from_user.id, res.amount+1)
    elif 2 < res.amount < 6:
        await message.reply(f'...')
        bot.database.set_amount(message.from_user.id, res.amount+1)
    elif res.amount == 6:
        await message.reply(f'Хм кажется у меня есть идея')
        bot.database.set_amount(message.from_user.id, res.amount+1)
    elif res.amount > 6:
        text = message.text.lower()
        if len(text.split()) == 2 and text.startswith("я"):
            text_split = text.split()
            await message.reply(f"Ты {text_split[1]}")
            bot.database.set_amount(message.from_user.id, res.amount + 1)
        else:
            await message.reply(message.text)
            bot.database.set_amount(message.from_user.id, res.amount+1)

if __name__ == "__main__":
    bot.run()
