from pyrogram import filters


def button_filter(button):
    async def func(_, __, message):
        return message.text == button.text
    return filters.create(func, 'ButtonFilter', button=button)


def inline_button_filter(button):
    async def func(_, __, query):
        return query.data == button.callback_data
    return filters.create(func, 'InlineButtonFilter', inline_button=button)


def reply_text_filter(text):
    async def func(_, __, message):
        return message.reply_to_message and message.reply_to_message.text == text
    return filters.create(func, 'ReplyTextFilter', text=text)
