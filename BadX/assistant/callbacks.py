from . import TheBadX

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from BadX.functions.messages import helpMessages
from BadX.functions.keyboard import help_buttons

@Client.on_callback_query(filters.regex("help:.*$"))
async def helpCallbacks(_, callback: CallbackQuery):
    query = str(callback.data.lower().split(":")[1])

    if query == "reboot":
        await callback.answer("Rebooting BadX.....", show_alert=True)
        await callback.message.edit("__🔸 Rebooting BadX.....__")
        await TheBadX.reboot()

    elif query == "spam":
        await callback.message.edit(
            helpMessages.spam.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "raid":
        await callback.message.edit(
            helpMessages.raid.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "direct":
        await callback.message.edit(
            helpMessages.direct_message.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "basic":
        await callback.message.edit(
            helpMessages.basic.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "profile":
        await callback.message.edit(
            helpMessages.profile.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "extra":
        await callback.message.edit(
            helpMessages.extra.format(TheBadX.handler, TheBadX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "back":
        await callback.message.edit(
            helpMessages.start.format(TheBadX.handler, TheBadX.updateChannel, TheBadX.supportGroup),
            reply_markup=help_buttons,
        )