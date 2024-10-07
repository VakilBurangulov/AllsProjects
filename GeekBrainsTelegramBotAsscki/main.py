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


if __name__ == "__main__":
    bot.run()
