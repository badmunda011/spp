import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheBotX

@Client.on_message(
    filters.command("ping", prefixes=TheBotX.handler) #& filters.user(TheBotX.sudo.sudoUsers)
)
async def ping(_, message: Message):
    if await TheBotX.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
    #u_time = int(int(time.time()) - int(TheBotX.startTime))
    #uptime = await TheBotX.functions.get_time(time=u_time)
    pong_msg = await message.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    try:
        await pong_msg.edit_text(f"⌾ {TheBotX.pingMsg} ⌾ \n\n ༝ ριиg 𝁂꯭꯭꯭֯  `{ms}` ᴍs \n ༝ νєяѕισи𝁂꯭꯭꯭֯  `{TheBotX.versions['BadX']}`")
    except:
        await pong_msg.edit_text(f"⌾ {TheBotX.pingMsg} ⌾ \n\n ༝ ριиg 𝁂꯭꯭꯭֯  `{ms}` ᴍs \n ༝ νєяѕισи𝁂꯭꯭꯭֯  `{TheBotX.versions['BadX']}`")
        await pong_msg.delete()
