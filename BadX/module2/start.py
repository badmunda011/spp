from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from . import TheBotX

START_PIC = START_PIC if START_PIC else "https://telegra.ph/file/6482940720892cb9a4479.jpg"

def get_start_buttons(username):
    START_OP = [
        [
            InlineKeyboardButton(
                text="🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url=f"https://t.me/ll_BAD_MUNDA_ll"
            ),
            InlineKeyboardButton(
                text="💥 sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/PBX_CHAT"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 👻",
                url=f"https://t.me/{username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url=f"https://t.me/HEROKUBIN_01/289"
            ),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇ ✨", url=f"https://t.me/HEROKUBIN_01"
            ),
        ],
    ]
    return START_OP

@Client.on_message(filters.command(["start"], prefixes=TheBotX.handler))
async def _start(BadX: Client, message: Message):
    global START_MESSAGE
    my_detail = await BadX.get_me()
    my_mention = my_detail.mention
    START_MESSAGE = START_MESSAGE if START_MESSAGE else f"ʜᴇʏ💫 {message.from_user.mention}🌸\n✥ ɪ ᴀᴍ {my_mention}\n\n❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠ�[...]"
    
    reply_markup = InlineKeyboardMarkup(get_start_buttons(my_detail.username))

    for i in range(1, 26):
        client = globals().get(f"Client{i}")
        if client:
            if ".jpg" in START_PIC or ".png" in START_PIC:
                await client.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=reply_markup,
                )
            elif ".mp4" in START_PIC.lower():
                await client.send_video(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=reply_markup,
                )
            else:
                await client.send_message(
                    message.chat.id,
                    START_MESSAGE,
                    reply_markup=reply_markup,
                )
