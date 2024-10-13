from pyrogram import filters


def button_filter(button):
    async def func(_, __, message):
        return message.text == button.text
    return filters.create(func, 'ButtonFilter', button=button)
