from pyrogram import filters


def button_filter(button):
    async def func(_, __, message):
        return message.text == button.text
    return filters.create(func, 'ButtonFilter', button=button)


def inline_button_filter(button):
    async def func(_, __, query):
        return query.data == button.callback_data
    return filters.create(func, 'InlineButtonFilter', inline_button=button)
