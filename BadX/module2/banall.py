from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ParseMode, ChatType
import asyncio
import os
import traceback
from unidecode import unidecode
import random 
import time
import requests

from . import TheBotX

@Client.on_message(
    filters.command("banall", prefixes=TheBotX.handler) & (filters.me | filters.user(TheBotX.sudo.sudoUsers))
)
async def ban_all(client, msg):
    chat_id = msg.chat.id    
    LOL = await msg.reply_text("hii")
    app = await client.get_me()
    BOT_ID = app.id
    x = 0
    bot = await client.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True    
    if bot_permission:
        banned_users = []
        async for member in client.get_chat_members(chat_id):       
            try:
                await client.ban_chat_member(chat_id, member.user.id) 
                x += 1
                await LOL.edit_text(f"✫ ᴜꜱᴇʀꜱ : {x} ✫")
            except Exception:
                pass
    else:
        await msg.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs.")


from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ParseMode, ChatType
import asyncio
import os
import traceback
from unidecode import unidecode
import random 
import time
import requests

from . import TheBotX

@Client.on_message(
    filters.command("unbanall", prefixes=TheBotX.handler) & (filters.me | filters.user(TheBotX.sudo.sudoUsers))
)
async def unban_all(client, msg):
    chat_id = msg.chat.id    
    LOL = await msg.reply_text("hii")
    app = await client.get_me()
    BOT_ID = app.id
    x = 0
    bot = await client.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True    
    if bot_permission:
        unbanned_users = []
        async for member in client.get_chat_members(chat_id, filter="kicked"):       
            try:
                await client.unban_chat_member(chat_id, member.user.id) 
                x += 1
                await LOL.edit_text(f"✫ ᴜꜱᴇʀꜱ ᴜɴʙᴀɴɴᴇᴅ: {x} ✫")
            except Exception:
                pass
    else:
        await msg.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀs.")
