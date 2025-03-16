import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheBotX

START_PIC = "https://telegra.ph/file/6482940720892cb9a4479.jpg"  # Start image/video

@Client.on_message(filters.command("start", prefixes=TheBotX.handler))
async def start(client: Client, message: Message):
    bot_info = await client.get_me()
    username = bot_info.username
    
    text = (
        f"ʜᴇʏ💫 {message.from_user.mention} 🌸\n"
        f"✥ ɪ ᴀᴍ {bot_info.mention}\n\n"
        "❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
        "Welcome to the bot!"
    )
    
    buttons = [
        [
            InlineKeyboardButton("🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url="https://t.me/ll_BAD_MUNDA_ll"),
            InlineKeyboardButton("💥 sᴜᴘᴘᴏʀᴛ 💥", url="https://t.me/PBX_CHAT"),
        ],
        [
            InlineKeyboardButton("👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 👻", url=f"https://t.me/{username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton("📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url="https://github.com/Badhacker98/Spam_X_bot/fork"),
            InlineKeyboardButton("✨ ᴜᴘᴅᴀᴛᴇ ✨", url="https://t.me/HEROKUBIN_01"),
        ],
    ]
    
    await client.send_photo(
        chat_id=message.chat.id,
        photo=START_PIC,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
