from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

start_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("❓Help"),
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)
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
            InlineKeyboardButton("🔹 Basic", "help:basic"),
            InlineKeyboardButton("Spam 🔹", "help:spam")
        ],
        [
            InlineKeyboardButton("🔹 DirectMessage (DM)", "help:direct"),
            InlineKeyboardButton("Raid 🔹", "help:Raid")
        ],
        [
            InlineKeyboardButton("🔹 Profile", "help:profile"),
            InlineKeyboardButton("Extra 🔹", "help:extra")
        ],
        [
            InlineKeyboardButton("🗑️", "client:close")
        ]
    ]
)

