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

@Client.on_inline_query(filters.regex("help_menu"))
async def inline_help(client: Client, inline_query):
    buttons, _ = await gen_inline_help_buttons(0, sorted(Config.CMD_MENU.keys()))
    help_text = await help_template("Owner Name", (len(Config.CMD_MENU), len(Config.BOT_CMD_MENU)), (0, 1))
    results = [
        InlineQueryResultPhoto(
            id="help_menu",
            photo_url="https://files.catbox.moe/paxel7.jpg",
            thumb_url="https://files.catbox.moe/paxel7.jpg",
            caption=help_text,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    ]
    await inline_query.answer(results, cache_time=0)
