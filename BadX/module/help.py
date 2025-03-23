from . import TheBadX
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    InlineQueryResultPhoto
)

@Client.on_message(
    filters.command("help", prefixes=TheBadX.handler)
)
async def help(_, message):
    if await TheBadX.sudo.sudoFilter(message, 3):  # sudo filter
        return

    # Define inline keyboard buttons (message ke liye)
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
                InlineKeyboardButton("🗑️ Close", callback_data="client:close")
            ]
        ]
    )

    await message.reply("Processing..", reply_markup=help_buttons)


@Client.on_inline_query(filters.regex("help_menu"))
async def inline_help(client: Client, inline_query):
    # Inline query ke liye `switch_inline_query_current_chat` use karo
    help_buttons = [
        [
            InlineKeyboardButton("🔹 Basic", switch_inline_query_current_chat="help basic"),
            InlineKeyboardButton("Spam 🔹", switch_inline_query_current_chat="help spam")
        ],
        [
            InlineKeyboardButton("🔹 DirectMessage (DM)", switch_inline_query_current_chat="help direct"),
            InlineKeyboardButton("Raid 🔹", switch_inline_query_current_chat="help raid")
        ],
        [
            InlineKeyboardButton("🔹 Profile", switch_inline_query_current_chat="help profile"),
            InlineKeyboardButton("Extra 🔹", switch_inline_query_current_chat="help extra")
        ],
        [
            InlineKeyboardButton("🗑️ Close", switch_inline_query_current_chat="")
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
