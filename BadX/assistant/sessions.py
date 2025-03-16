import asyncio

from . import TheBadX
from BadX.config import API_ID, API_HASH
from BadX.functions.keyboard import gen_inline_keyboard

from pyrogram import Client, filters
from pyrogram.types import WebAppInfo
from pyrogram.types import (
    Message,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from pyrogram.errors import (
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)


@Client.on_message(
    filters.regex("🔸 Get All Clients 🔸") & filters.private  # & filters.user(TheBadX.sudo.sudoUsers)
)
async def get_all_clients(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 2):
        return
    if len(TheBadX.clients) == 0:
        await message.reply("__You have 0 clients__")
        return
    wait = await message.reply("__getting clients__ ....", reply_markup=ReplyKeyboardRemove())
    clientText = f"**{TheBadX.BadX.me.mention} all Clients**\n\n"
    clientNo = 0
    for client in TheBadX.clients:
        clientNo += 1
        clientText += f"**{clientNo})** {client.me.mention}, User ID: `{client.me.id}`\n"

    clientText += f"\n **Total: {clientNo}**, __For full details type /get (user ID)__"
    await message.reply(clientText)
    await wait.delete()


@Client.on_message(
    filters.private & filters.command("get")
)
async def get_client(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    try:
        user_id = int(message.command[1])
    except:
        await message.reply("__Invalid! please share phone number (without '+') or user ID.__")
        return
    wait = await message.reply(f"__getting {user_id} in DB.....__")
    clientNo = 0
    for c in TheBadX.clients:
        clientNo += 1
        if c.me.id == user_id:
            client = c
            break
        else:
            client = None

    if client:
        details = "**BadX Clients details** \n\n"
        details += f" **- Number: {clientNo}** \n"
        if client.me.is_bot:
            details += " **- Type: Bot** \n"
        else:
            details += " **- Type: User** \n"
        details += f" **- Name:** {client.me.mention} \n"
        details += f" **- User ID:** {client.me.id} \n"
        if not client.me.is_bot:
            details += f" **- Phone No.:** `+{client.me.phone_number}` \n"
        await message.reply(
            details,
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.reply(f"__No any active client with user ID - {user_id}.__")
    await wait.delete()


@Client.on_message(
    filters.regex("➕ New Client") & filters.private  # & filters.user(TheBadX.sudo.sudoUsers)
)
async def new_session(_, message: Message):
    await message.reply_text(
        "**𝖮𝗄𝖺𝗒!** 𝖫𝖾𝗍'𝗌 𝗌𝖾𝗍𝗎𝗉 𝖺 𝗇𝖾𝗐 𝗌𝖾𝗌𝗌𝗂𝗈𝗇",
        reply_markup=ReplyKeyboardRemove(),
    )

    buttons = [
        [
            InlineKeyboardButton(
                " ɢᴇɴʀᴀᴛᴇ ɴᴇᴡ ᴄʟɪᴇɴᴛ", 
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user")
            ),
        ]
    ]

    await message.reply_text(
        "👻 ɢᴇɴʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ☠️ ",
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@Client.on_message(
    filters.private & filters.command("add")
)
async def add_client(RiZoeL: Client, message: Message):
    if await TheBadX.sudo.sudoFilter(message):
        return
    try:
        session_string = message.command[1]
    except IndexError:
        await message.reply("__Invalid! Please provide a session string.__")
        return

    checking = await message.reply("__checking...__")

    BadXClient = Client(
        f"BadX-{session_string[:10]}",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
        plugins=dict(root="BadX.module")
    )
    try:
        await BadXClient.start()
        TheBadX.clients.append(BadXClient)
        TheBadX.database.addSession(BadXClient.me.id, session_string)
        await message.reply(f"**✅ Wew, Client {BadXClient.me.mention} Started**")
    except Exception as er:
        await message.reply(f"**❎ Error:** {str(er)} \n\n __Report in @{TheBadX.supportGroup}__")
    await checking.delete()
    


@Client.on_message(
    filters.regex("➕ Add Client") & filters.private  # & filters.user(TheBadX.sudo.sudoUsers)
)
async def session_add(_, message: Message):
    await message.reply_text("/add {ᴘᴀsᴛᴇ ʏᴏᴜʀ ᴘʏ2 sᴇssɪᴏɴ} ✓ ❤️")


@Client.on_message(
    filters.regex("Remove Client ➖") & filters.private  # & filters.user(TheBadX.sudo.sudoUsers)
)
async def remove_client(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    if len(TheBadX.clients) == 0:
        await message.reply_text("❎ No clients found in Database.")
        return

    process = await message.reply("__processing....__", reply_markup=ReplyKeyboardRemove())

    collection = []
    clientNo = 0
    for client in TheBadX.clients:
        if client.me.is_bot:
            collection.append((f"Bot: {client.me.id}", f"client:delete:{client.me.id}:{clientNo}"))
        else:
            collection.append((f"+{client.me.phone_number}", f"client:delete:{client.me.phone_number}:{clientNo}"))
        clientNo += 1

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "auth_close")])

    await message.reply_text(
        "**▪️ Choose Client to remove:**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    await process.delete()


@Client.on_message(
    filters.regex("🔐 Get Access Of Client") & filters.private  # & filters.user(TheBadX.sudo.sudoUsers)
)
async def get_access(_, message: Message):
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    if len(TheBadX.clients) == 0:
        await message.reply_text("❎ No clients found in Database.")
        return

    process = await message.reply("__processing....__", reply_markup=ReplyKeyboardRemove())

    collection = []
    clientNo = 0
    for client in TheBadX.clients:
        if not client.me.is_bot:
            collection.append((f"+{client.me.phone_number}", f"client:access:{client.me.phone_number}:{clientNo}"))
        clientNo += 1

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "client:close")])

    await message.reply_text(
        "**▪️ Choose Client to access:**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    await process.delete()


@Client.on_callback_query(filters.regex("client:.*$"))
async def clientCallbacks(_, callback: CallbackQuery):
    if await TheBadX.sudo.sudoFilter(callback.message, 1, callback.from_user.id):
        await callback.message.delete()
        return

    if callback.data.split(":")[1] == "close":
        await callback.message.delete()
        return

    if callback.data.split(":")[1] == "back":
        await callback.answer("processing.....", show_alert=True)
        collection = []
        clientNo = 0
        if callback.data.split(':')[2].lower() == "access":
            for client in TheBadX.clients:
                if not client.me.is_bot:
                    collection.append((f"+{client.me.phone_number}", f"client:access:{client.me.phone_number}:{clientNo}"))
                    clientNo += 1

        elif callback.data.split(':')[2].lower() == "delete":
            for client in TheBadX.clients:
                if client.me.is_bot:
                    collection.append((f"Bot: {client.me.id}", f"client:delete:{client.me.id}:{clientNo}"))
                else:
                    collection.append((f"+{client.me.phone_number}", f"client:delete:{client.me.phone_number}:{clientNo}"))
                clientNo += 1

        buttons = gen_inline_keyboard(collection, 2)
        buttons.append([InlineKeyboardButton("Cancel ❌", "client:close")])

        try:
            await callback.message.edit(
                f"**Choose Client to {callback.data.split(':')[2]}:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except:
            await callback.message.reply_text(
                "**Choose Client to remove:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            await callback.message.delete()
        return

    query = callback.data.split(":")
    func = str(query[1].lower())
    phone_id = int(query[2].lower())
    client_number = int(query[3].lower())
    if func == "delete":
        try:
            await callback.message.edit(
                f"**Please confirm that you want to remove {TheBadX.clients[client_number].me.mention} ({phone_id}) from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("✅ Yes", f"client:remove:{phone_id}:{client_number}"),
                            InlineKeyboardButton("No ❎", "client:close")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                )
            )
        except:
            await callback.message.reply(
                f"**Please confirm that you want to remove {TheBadX.clients[client_number].me.mention} ({phone_id}) from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("✅ Yes", f"client:remove:{phone_id}:{client_number}"),
                            InlineKeyboardButton("No ❎", "client:close")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                )
            )
            await callback.message.delete()

    elif func == "remove":
        await callback.answer("removing...", show_alert=True)
        await callback.message.edit("__removing__")
        client = TheBadX.clients[client_number]
        await client.stop()
        client_mention = client.me.mention
        TheBadX.clients.remove(client)

        try:
            await callback.message.edit(
                f"**Removed {client_mention} from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                ),
            )
        except:
            await callback.message.reply_text(
                f"**Removed {client_mention} from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                ),
            )
            await callback.message.delete()

    elif func == "access":
        try:
            await callback.message.edit(
                f"**🕹️ You can access your client using this panel!** \n\n **Phone Number:**  {phone_id}  __(tap to copy)__ \n\n **Note:** First Login number on telegram then click on 'Get OTP'",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Get OTP 🔑", f"client:otp:{phone_id}:{client_number}")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:access")
                        ]
                    ]
                )
            )
        except:
            await callback.message.reply_text(
                f"**🕹️ You can access your client using this panel!** \n\n **Phone Number:**  {phone_id}  __(tap to copy)__ \n\n **Note:** First Login number on telegram then click on 'Get OTP'",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Get OTP 🔑", f"client:otp:{phone_id}:{client_number}")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:access")
                        ]
                    ]
                )
            )
            await callback.message.delete()

    elif func == "otp":
        await callback.message.edit("__fetching.....__")
        client = TheBadX.clients[client_number]
        async for otp_message in client.get_chat_history(777000, 1):
            if otp_message.text.lower().startswith("login code:"):
                otp_is = int(otp_message.text.split(" ")[2].split(".")[0])
            else:
                otp_is = None
                try:
                    await callback.message.edit(
                        f"**🤷 I didn't received any OTP on {phone_id}**",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Get OTP again 🔑", f"client:otp:{phone_id}:{client_number}")
                                ],
                                [
                                    InlineKeyboardButton("🔙", "client:back:access")
                                ]
                            ]
                        )
                    )
                except:
                    await callback.message.reply_text(
                        f"**🤷 I didn't received any OTP on {phone_id}**",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Get OTP again 🔑", f"client:otp:{phone_id}:{client_number}")
                                ],
                                [
                                    InlineKeyboardButton("🔙", "client:back:access")
                                ]
                            ]
                        )
                    )
                    await callback.message.delete()
        if otp_is:
            session_data = TheBadX.database.getSession(phone_id)
            if session_data['password']:
                otp_text = f"**🔑 OTP for {phone_id} is:**\n\n**🔐 OTP -**  `{otp_is}`  __(tap to copy)__ \n**🔓 Password -** `{session_data['password']}`"
            else:
                otp_text = f"**🔑 OTP for {phone_id} is**  `{otp_is}`  __(tap to copy)__"
            try:
                await callback.message.edit(
                    otp_text,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔙", "client:back:access")
                            ]
                        ]
                    )
                )
            except:
                await callback.message.delete()
