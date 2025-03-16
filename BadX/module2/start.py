from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from . import TheBotX

START_PIC = "https://telegra.ph/file/6482940720892cb9a4479.jpg"  # Start image/video

def get_start_buttons(username):
    return [
        [
            InlineKeyboardButton("🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url="https://t.me/ll_BAD_MUNDA_ll"),
            InlineKeyboardButton("💥 sᴜᴘᴘᴏʀᴛ 💥", url="https://t.me/PBX_CHAT"),
        ],
        [
            InlineKeyboardButton("👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 👻", url=f"https://t.me/{username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton("📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url="https://t.me/HEROKUBIN_01/289"),
            InlineKeyboardButton("✨ ᴜᴘᴅᴀᴛᴇ ✨", url="https://t.me/HEROKUBIN_01"),
        ],
    ]

@Client.on_message(filters.command(["start"], prefixes=TheBotX.handler))
async def start_command(client: Client, message: Message):
    bot_info = await client.get_me()
    start_message = (
        f"ʜᴇʏ💫 {message.from_user.mention} 🌸\n"
        f"✥ ɪ ᴀᴍ {bot_info.mention}\n\n"
        "❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
        "Welcome to the bot!"
    )

    reply_markup = InlineKeyboardMarkup(get_start_buttons(bot_info.username))

    try:
        if START_PIC.endswith((".jpg", ".png")):
            await client.send_photo(message.chat.id, START_PIC, caption=start_message, reply_markup=reply_markup)
        elif START_PIC.endswith(".mp4"):
            await client.send_video(message.chat.id, START_PIC, caption=start_message, reply_markup=reply_markup)
        else:
            await client.send_message(message.chat.id, start_message, reply_markup=reply_markup)
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {str(e)}")
