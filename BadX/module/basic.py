import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheBadX

@Client.on_message(
    filters.command("ping", prefixes=TheBadX.handler) #& filters.user(TheBadX.sudo.sudoUsers)
)
async def ping(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
    #u_time = int(int(time.time()) - int(TheBadX.startTime))
    #uptime = await TheBadX.functions.get_time(time=u_time)
    pong_msg = await message.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    try:
        await pong_msg.edit_text(f"⌾ {TheBadX.pingMsg} ⌾ \n\n ༝ ριиg 𝁂꯭꯭꯭֯  `{ms}` ᴍs \n ༝ νєяѕισи𝁂꯭꯭꯭֯  `{TheBadX.versions['BadX']}`")
    except:
        await pong_msg.edit_text(f"⌾ {TheBadX.pingMsg} ⌾ \n\n ༝ ριиg 𝁂꯭꯭꯭֯  `{ms}` ᴍs \n ༝ νєяѕισи𝁂꯭꯭꯭֯  `{TheBadX.versions['BadX']}`")
        await pong_msg.delete()

@Client.on_message(
    filters.command("alive", prefixes=TheBadX.handler) #& filters.user(TheBadX.sudo.sudoUsers)
)
async def alive(BadX: Client, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 3):
        return
    await TheBadX.functions.send_alive(BadX, message)

@Client.on_message(
    filters.command("limit", prefixes=TheBadX.handler) #& filters.user(TheBadX.sudo.sudoUsers)
)
async def check_limit(BadX: Client, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 3):
        return
    if BadX.me.is_bot:
        return
    event = await message.reply_text("__Checking your account for Spambot...__")
    try:
        await BadX.unblock_user("spambot")
        await BadX.send_message("spambot", "/start")
        await asyncio.sleep(2)
        async for history in BadX.get_chat_history("spambot", limit=1):
            await TheBadX.functions.delete_reply(message, event, str(history.text))
    except Exception as error:
        await TheBadX.functions.delete_reply(message, event, str(error))

@Client.on_message(
    filters.command(["help", "restart", "reboot"], prefixes=TheBadX.handler) #& filters.user(TheBadX.sudo.sudoUsers)
)
async def help_reboot(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 3):
        return
    if "reboot" or "restart" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheBadX.BadX.me.username}?start=reboot) to reboot your BadX!**",
            disable_web_page_preview=True,
        )
    elif "help" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheBadX.BadX.me.username}?start=help) for help menu of BadX!**",
            disable_web_page_preview=True,
        )

@Client.on_message(filters.command(["stats", "stat"], prefixes=TheBadX.handler))
async def stats(BadX: Client, message: Message):
    if BadX.me.is_bot:
        await message.reply("__This command is only for id not for bot__")
        return
    if await TheBadX.sudo.sudoFilter(message):
        return
    wait = await message.reply_text("collecting....")
    start = datetime.datetime.now()
    private = 0
    gc = 0
    super_gc = 0
    channel = 0
    bot = 0
    admin_gc = 0
    async for dialog in BadX.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            private += 1
        elif dialog.chat.type == ChatType.BOT:
            bot += 1
        elif dialog.chat.type == ChatType.GROUP:
            gc += 1
        elif dialog.chat.type == ChatType.SUPERGROUP:
            super_gc += 1
            admin = await dialog.chat.get_member(int(BadX.me.id))
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                admin_gc += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            channel += 1

    end = datetime.datetime.now()
    ms = (end - start).seconds
    stats = f"{BadX.me.first_name}'s stats \n\n"
    stats += "------------- » «» « ------------- \n"
    stats += f"Private Messages: `{private}` \n"
    stats += f"Bots in Inbox: `{bot}` \n"
    stats += f"Total Groups: `{gc}` \n"
    stats += f"Total Super Groups: `{super_gc}` \n"
    stats += f"Total Channels: `{channel}` \n"
    stats += f"Admin in: `{admin_gc}` chats \n\n"
    stats += "------------- » «» « ------------- \n\n"
    stats += f"Time Taken `{ms}secs` \n"
    stats += f"© @{TheBadX.updateChannel}"
    await TheBadX.functions.delete_reply(message, wait, stats)
