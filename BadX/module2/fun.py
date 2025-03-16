from . import TheBotX

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["echo", "repeat"], prefixes=TheBotX.handler))
async def echo(BadX: Client, message: Message):
    if await TheBotX.sudo.sudoFilter(message, 3):
        return
    txt = ' '.join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(f"**Wrong Usage!** \n\n __- Syntax:__ `{TheBotX.handler}echo` (message or reply to message)")
        return

    try:
        await message.delete()
        await BadX.send_message(message.chat.id, msg)
    except Exception as a:
        await BadX.send_message(message.chat.id, msg)
