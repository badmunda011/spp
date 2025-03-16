from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
import asyncio
from . import TheBotX

# Command to ban all members
@Client.on_message(filters.command(["banall"], prefixes=TheBotX.handler))
async def ban_all(client, message):
    chat_id = message.chat.id
    async for member in client.iter_chat_members(chat_id):
        if member.user.is_bot or member.user.id in sudo_users:
            continue
        try:
            await client.kick_chat_member(chat_id, member.user.id)
            await asyncio.sleep(0.1)  # Adjust sleep to control speed
        except Exception as e:
            print(f"Failed to ban {member.user.id}: {e}")

# Command to unban all members
@Client.on_message(filters.command(["unbanall"], prefixes=TheBotX.handler))
async def unban_all(client, message):
    chat_id = message.chat.id
    banned_users = await client.get_chat_members(chat_id, filter="kicked")
    for user in banned_users:
        try:
            await client.unban_chat_member(chat_id, user.user.id)
            await asyncio.sleep(0.5)  # Adjust sleep to control speed
        except Exception as e:
            print(f"Failed to unban {user.user.id}: {e}")

