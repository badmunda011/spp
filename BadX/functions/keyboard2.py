from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

start_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔹 ғᴇᴀᴛᴜʀᴇs 🔹")
        ],
        [
            KeyboardButton(" ʜᴇʟᴘ❓"),
            KeyboardButton(" ᴏᴛʜᴇʀs ↗️")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

manage_clients_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸ɢᴇᴛ ᴀʟʟ ᴄʟɪᴇɴᴛs🔸")
        ],
        [
            KeyboardButton("➕ ᴀᴅᴅ ᴜsᴇʀs"),
            KeyboardButton("ʀᴇᴍᴏᴠᴇ ᴜsᴇʀs ➖")
        ],
        [
            KeyboardButton("🔐 ɢᴇᴛ ᴀᴄᴄᴇss ᴏғ ᴄʟɪᴇɴᴛ")
        ],
        [
            KeyboardButton("ʜᴏᴍᴇ 🏠")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

other_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("↗️  ᴊᴏɪɴ ᴀʟʟ ɢʀᴏᴜᴘ "),
            KeyboardButton("ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ ↙️")
        ],
        [
            KeyboardButton("👥 sᴜᴅᴏ ᴜsᴇʀs"),
            KeyboardButton("ᴀᴄᴛɪᴠᴇ ᴛᴀsᴋs ℹ️")
        ],
        [
            KeyboardButton("🔒 ʀᴇsᴛʀɪᴄᴛɪᴏɴs")
        ],
        [
            KeyboardButton("ʜᴏᴍᴇ 🏠")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

sudo_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸 ɢᴇᴛ ᴀʟʟ sᴜᴅᴏs🔸")
        ],
        [
            KeyboardButton("➕ ᴀᴅᴅ sᴜᴅᴏ"),
            KeyboardButton("ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ➖")
        ],
        [
            KeyboardButton("ʀᴇᴍᴏᴠᴇ ᴀʟʟ sᴜᴅᴏ ☑️")
        ],
        [
            KeyboardButton("🔙")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

restriction_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸 ɢᴇᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄʜᴀᴛs 🔸")
        ],
        [
            KeyboardButton("➕ ᴀᴅᴅ ᴄʜᴀᴛ"),
            KeyboardButton("ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ ➖")
        ],
        [
            KeyboardButton("🔙")
        ]
    ],
    resize_keyboard=True,
)

# --- funcs --- #
def btn(text, value, type="callback_data") -> InlineKeyboardButton:
    return InlineKeyboardButton(text, **{type: value})

def gen_inline_keyboard(collection: list, row: int = 2) -> list[list[InlineKeyboardButton]]:
    keyboard = []
    for i in range(0, len(collection), row):
        kyb = []
        for x in collection[i : i + row]:
            button = btn(*x)
            kyb.append(button)
        keyboard.append(kyb)
    return keyboard

# ---- Inline ---- #
help_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔹 ʙᴀsɪᴄ", "help:basic"),
            InlineKeyboardButton("sᴘᴀᴍ 🔹", "help:spam")
        ],
        [
            InlineKeyboardButton("🔹 ᴅɪʀᴇᴄᴛ ᴍsɢ (ᴅᴍ)", "help:direct"),
            InlineKeyboardButton("ʀᴀɪᴅ 🔹", "help:Raid")
        ],
        [
            InlineKeyboardButton("🔹 ᴘʀᴏғɪʟᴇ", "help:profile"),
            InlineKeyboardButton("ᴇxᴛʀᴀ 🔹", "help:extra")
        ],
        [
            InlineKeyboardButton("ᴄʟᴏsᴇ", "client:close")
        ]
    ]
)

reboot_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʀᴇʙᴏᴏᴛ 🔄", "help:reboot")
        ]
    ]
)
