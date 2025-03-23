import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheBadX

@Client.on_message(
    filters.command("ping", prefixes=TheBadX.handler) #& filters.user(TheBadX.sudo.sudoUsers)
)
async def ping(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
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

@Client.on_inline_query(filters.regex("ping_menu"))
async def inline_ping(client: Client, inline_query):
    img = await db.get_env(ENV.ping_pic)
    if not img:
        img = "https://telegra.ph/file/14166208a7bf871cb0aca.jpg"  # Default image

    uptime = readable_time(time.time() - START_TIME)
    
    # Speed calculation ka seedha tareeka, bas inline query receive hone ka time le rahe hain
    start_time = time.time()
    speed = round(time.time() - start_time, 3)

    caption = await ping_template(speed, uptime, inline_query.from_user.mention)

    buttons = [
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/PBX_CHAT"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/HEROKUBIN_01"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    results = [
        InlineQueryResultPhoto(
            photo_url=img,
            thumb_url=img,
            caption=caption,
            reply_markup=reply_markup,
        )
    ]

    await inline_query.answer(results, cache_time=0)
