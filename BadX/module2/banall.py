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
