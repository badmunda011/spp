from . import TheBadX

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["gcast", "broadcast"], prefixes=TheBadX.handler)
)
async def broadcast(BadX: Client, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 1):
        return

    await TheBadX.functions.broadcast(BadX, message)

@Client.on_message(
    filters.command('join', prefixes=TheBadX.handler)
)
async def join(BadX: Client, message: Message):
    try:
        group = str(message.command[1])
    except:
        await message.reply("__Please give valid join link or username of group to join.__")
        return

    wait = await message.reply("__joining.....__")
    try:
        await BadX.join_chat(group)
        await message.reply("**✅ Joined successfully**")
    except Exception as er:
        await message.reply(f"**Error while join:** {str(er)} \n\n__Report in @{TheBadX.supportGroup}__")
    await wait.delete()

@Client.on_message(
    filters.command(["leave", "left"], prefixes=TheBadX.handler)
)
async def leave(BadX: Client, message: Message):
    if len(message.command) == 1:
        group = message.chat.id
    else:
        try:
            group = message.command[1]
        except:
            await message.reply("__Please give valid join link or username of group to join.__")
            return

    if group in [TheBadX.restrict.res, f"@{TheBadX.supportGroup}", f"@{TheBadX.updateChannel}", TheBadX.supportGroup, TheBadX.updateChannel]:
        return

    wait = await message.reply("__leaving.....__")
    try:
        await BadX.join_chat(group)
        await message.reply("**✅ Left successfully**")
    except Exception as er:
        await message.reply(f"**Error while Leave:** {str(er)} \n\n__Report in @{TheBadX.supportGroup}__")
    await wait.delete() 