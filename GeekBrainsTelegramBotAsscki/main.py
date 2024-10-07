# import packages inside python
import random

# import downloaded packages
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, ForceReply
import requests

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
        if message.text.lower() == "я дурак":
            await message.reply("Ты дурак")
            bot.database.set_amount(message.from_user.id, res.amount + 1)
        else:
            await message.reply(message.text)
            bot.database.set_amount(message.from_user.id, res.amount+1)

if __name__ == "__main__":
    bot.run()
