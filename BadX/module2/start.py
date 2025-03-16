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
