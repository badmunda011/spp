from . import TheBadX
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto

@Client.on_message(
    filters.command("help", prefixes=TheBadX.handler)
)
async def hi(_, message):
    if await TheBadX.sudo.sudoFilter(message, 3): # sudo filter
        return

    # Define inline keyboard buttons
    help_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔹 Basic", callback_data="help:basic"),
                InlineKeyboardButton("Spam 🔹", callback_data="help:spam")
            ],
            [
                InlineKeyboardButton("🔹 DirectMessage (DM)", callback_data="help:direct"),
                InlineKeyboardButton("Raid 🔹", callback_data="help:Raid")
            ],
            [
                InlineKeyboardButton("🔹 Profile", callback_data="help:profile"),
                InlineKeyboardButton("Extra 🔹", callback_data="help:extra")
            ],
            [
                InlineKeyboardButton("🗑️", callback_data="client:close")
            ]
        ]
    )
    
    await message.reply("processing..", reply_markup=help_buttons)

@Client.on_inline_query(filters.regex("help_menu"))
async def inline_help(client: Client, inline_query):
    help_buttons = [
        [
            InlineKeyboardButton("🔹 Basic", callback_data="help:basic"),
            InlineKeyboardButton("Spam 🔹", callback_data="help:spam")
        ],
        [
            InlineKeyboardButton("🔹 DirectMessage (DM)", callback_data="help:direct"),
            InlineKeyboardButton("Raid 🔹", callback_data="help:Raid")
        ],
        [
            InlineKeyboardButton("🔹 Profile", callback_data="help:profile"),
            InlineKeyboardButton("Extra 🔹", callback_data="help:extra")
        ],
        [
            InlineKeyboardButton("🗑️", callback_data="client:close")
        ]
    ]
    results = [
        InlineQueryResultPhoto(
            id="help_menu",
            photo_url="https://files.catbox.moe/paxel7.jpg",
            thumb_url="https://files.catbox.moe/paxel7.jpg",
            caption="Select an option from below",
            reply_markup=InlineKeyboardMarkup(help_buttons),
        )
    ]
    await inline_query.answer(results, cache_time=0)
