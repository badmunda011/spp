import glob
import importlib
import os
import sys
from pathlib import Path

import pyroaddon
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BadX import (
    UpdateChannel,
    SupportGroup,
    dataBase,
    version,
    pingMSG,
    StartTime,
    activeTasks,
)
from BadX.config import (
    API_ID,
    API_HASH,
    ASSISTANT_TOKEN,
    LOGGER_ID,
    OWNER_ID,
    HANDLER,
)
from .core import sudoers, restriction, functions
from .messages import helpMessages
from .keyboard import help_buttons
from .logger import LOGS

devs = [7588172591]

class BadX(Client):
    def __init__(self) -> None:
        self.clients: list[Client] = []
        self.BadX: Client = Client(
            "BadX Assistant",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=ASSISTANT_TOKEN,
            plugins=dict(root="BadX.assistant")
        )
        self.database = dataBase
        self.loggerID = LOGGER_ID
        self.updateChannel = UpdateChannel
        self.supportGroup = SupportGroup
        self.author = "II_BAD_BABY_II"
        self.versions = version
        self.logs = LOGS
        self.sudo = sudoers
        self.owner_id = OWNER_ID
        self.restrict = restriction
        self.functions = functions
        self.handler = HANDLER
        self.pingMsg = pingMSG
        self.startTime = StartTime
        self.activeTasks = activeTasks
        self.dev = devs
        self.logo= "https://telegra.ph/file/3e28ce1ed1a89395ac07b.jpg"

    async def StartAllClients(self):
        LOGS.info("Loading all sessions.....")
        sessions_list = self.database.getAllSessions()
        if len(sessions_list) == 0:
            LOGS.info("-> 0 Client - Add clients after starting assistant, starting assistant...!")
        else:
            LOGS.info(f"-> Loaded {len(sessions_list)} session let's start BadX clients")
            bots = 0
            users = 0
            for session_data in sessions_list:
                phone_number = session_data["phone_number"]
                client_session = str(session_data["session"])
                if client_session:
                    type = await self.clientType(str(client_session))
                    if type == "bot":
                        BadXClient = Client(
                            f"BadX-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            bot_token=client_session,
                            plugins=dict(root="BadX.module")
                            )
                    else:
                        BadXClient = Client(
                            f"BadX-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            session_string=client_session,
                            plugins=dict(root="BadX.module")
                            )
                    try:
                        await BadXClient.start()
                        if type == "user":
                            try:
                                await BadXClient.join_chat(UpdateChannel)
                                await BadXClient.join_chat(SupportGroup)
                                try:
                                    await BadXClient.send_message(self.BadX.me.username, "/start")
                                except:
                                    pass
                            except Exception:
                                pass
                            users += 1
                        else:
                            bots += 1
                        self.clients.append(BadXClient)
                    except Exception:
                        LOGS.error(f"Error while start {phone_number} - {type}, skipping this...")
                        dataBase.removeSession(phone_number)
                else:
                    dataBase.removeSession(phone_number)
            LOGS.info(f"Started {len(self.clients)} BadX Clients (User - {users} | Bots - {bots})")

    async def startBot(self) -> None:
        await self.BadX.start()
        LOGS.info(f"-> Started BadX Client: '{self.BadX.me.username}'")

    async def clientType(self, session: str) -> str:
        if ":" in session and session.split(":")[0].isnumeric():
            return "bot"
        else:
            return "user"

    async def validateLogger(self, client: Client) -> bool:
        try:
            await client.get_chat_member(LOGGER_ID, "me")
            return True
        except Exception:
            return await self.joinLogger(client)

    async def joinLogger(self, client: Client) -> bool:
        try:
            invite_link = await self.BadX.export_chat_invite_link(LOGGER_ID)
            await client.join_chat(invite_link)
            return True
        except Exception:
            return False

    async def stopAllClients(self):
        clientNo = 0
        for client in self.clients:
            clientNo += 1
            try:
                await client.stop()
            except Exception as error:
                self.logs.info(f"Error while stopping client!: {str(error)}")

    async def startMessage(self) -> None:
        log_text = "**BadX is Now Alive** \n\n"
        log_text += f"**BadX Clients:** __{len(self.clients)}\n\n"
        log_text += "Versions:\n"
        log_text += f"   ~ BadX: {self.versions['BadX']} \n"
        log_text += f"   ~ PyroGram: {self.versions['pyrogram']} \n"
        log_text += f"   ~ Python: {self.versions['python']}"
        try:
            await self.BadX.send_photo(
                self.loggerID,
                "https://telegra.ph/file/3e28ce1ed1a89395ac07b.jpg",
                caption=log_text,
                parse_mode=ParseMode.MARKDOWN,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Start me", url=f"https://t.me/{self.BadX.me.username}?start=start"),
                        ],
                        [
                            InlineKeyboardButton("channel", url=f"https://t.me/{self.updateChannel}"),
                            InlineKeyboardButton("support", url=f"https://t.me/{self.supportGroup}"),
                        ],
                    ]
                ),
            )
        except Exception as e:
            self.logs.error(f"Error sending start message: {e}")

    async def reboot(self) -> None:
        try:
            await self.BadX.stop()
        except Exception as error:
            self.logs.info(str(error))

        await self.stopAllClients()

        args = [sys.executable, "-m", "BadX"]
        os.execl(sys.executable, *args)
        quit()

    async def help(self, chat_id: int) -> None:
        try:
            await self.BadX.send_photo(
                chat_id,
                self.logo,
                helpMessages.start.format(self.handler, self.updateChannel, self.supportGroup),
                reply_markup=help_buttons,
            )
        except Exception as er:
            await self.BadX.send_message(
                chat_id,
                f"**Error:** {str(er)} \n\n__Report in @{self.supportGroup}__"
            )

    async def loadPlugs(self) -> None:
        count = 0
        files = glob.glob("BadX/assistant/*.py")
        for file in files:
            with open(file) as f:
                path = Path(f.name)
                shortname = path.stem.replace(".py", "")
                if shortname.startswith("__"):
                    continue
                fpath = Path(f"BadX/assistant/{shortname}.py")
                name = "BadX.assistant." + shortname
                spec = importlib.util.spec_from_file_location(name, fpath)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["BadX.assistant." + shortname] = load
                count += 1
            f.close()
        LOGS.info(
            f"- > Loaded User Plugin: '{count}'"
        )

    async def startup(self) -> None:
        LOGS.info(
            f"-> Starting BadX ....."
        )
        await self.startBot()
        await self.StartAllClients()
        #await self.loadPlugs()
        await self.sudo.loadSudo()
        await self.restrict.loadRestrictChats()
        await self.startMessage()

TheBadX = BadX()

class BotX(Client):
    def __init__(self) -> None:
        self.clients: list[Client] = []
        self.BotX: Client = Client(
            "BotX Assistant",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=ASSISTANT_TOKEN,
            plugins=dict(root="BadX.assistant")
        )
        self.database = dataBase
        self.loggerID = LOGGER_ID
        self.updateChannel = UpdateChannel
        self.supportGroup = SupportGroup
        self.author = "II_BAD_BABY_II"
        self.versions = version
        self.logs = LOGS
        self.sudo = sudoers
        self.owner_id = OWNER_ID
        self.restrict = restriction
        self.functions = functions
        self.handler = HANDLER
        self.pingMsg = pingMSG
        self.startTime = StartTime
        self.activeTasks = activeTasks
        self.dev = devs
        self.logo= "https://telegra.ph/file/3e28ce1ed1a89395ac07b.jpg"

    async def StartAllClients(self):
        LOGS.info("Loading all sessions.....")
        sessions_list = self.database.getAllSessions()
        if len(sessions_list) == 0:
            LOGS.info("-> 0 Client - Add clients after starting assistant, starting assistant...!")
        else:
            LOGS.info(f"-> Loaded {len(sessions_list)} session let's start BotX clients")
            bots = 0
            users = 0
            for session_data in sessions_list:
                phone_number = session_data["phone_number"]
                client_session = str(session_data["session"])
                if client_session:
                    type = await self.clientType(str(client_session))
                    if type == "bot":
                        BotXClient = Client(
                            f"BotX-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            bot_token=client_session,
                            plugins=dict(root="BadX.module")
                            )
                    else:
                        BotXClient = Client(
                            f"BotX-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            session_string=client_session,
                            plugins=dict(root="BadX.module")
                            )
                    try:
                        await BotXClient.start()
                        if type == "user":
                            try:
                                await BotXClient.join_chat(UpdateChannel)
                                await BotXClient.join_chat(SupportGroup)
                                try:
                                    await BotXClient.send_message(self.BotX.me.username, "/start")
                                except:
                                    pass
                            except Exception:
                                pass
                            users += 1
                        else:
                            bots += 1
                        self.clients.append(BotXClient)
                    except Exception:
                        LOGS.error(f"Error while start {phone_number} - {type}, skipping this...")
                        dataBase.removeSession(phone_number)
                else:
                    dataBase.removeSession(phone_number)
            LOGS.info(f"Started {len(self.clients)} BotX Clients (User - {users} | Bots - {bots})")

    async def startBot(self) -> None:
        await self.BotX.start()
        LOGS.info(f"-> Started BotX Client: '{self.BotX.me.username}'")

    async def clientType(self, session: str) -> str:
        if ":" in session and session.split(":")[0].isnumeric():
            return "bot"
        else:
            return "user"

    async def validateLogger(self, client: Client) -> bool:
        try:
            await client.get_chat_member(LOGGER_ID, "me")
            return True
        except Exception:
            return await self.joinLogger(client)

    async def joinLogger(self, client: Client) -> bool:
        try:
            invite_link = await self.BotX.export_chat_invite_link(LOGGER_ID)
            await client.join_chat(invite_link)
            return True
        except Exception:
            return False

    async def stopAllClients(self):
        clientNo = 0
        for client in self.clients:
            clientNo += 1
            try:
                await client.stop()
            except Exception as error:
                self.logs.info(f"Error while stopping client!: {str(error)}")

    async def startMessage(self) -> None:
        log_text = "**BotX is Now Alive** \n\n"
        log_text += f"**BotX Clients:** __{len(self.clients)}\n\n"
        log_text += "Versions:\n"
        log_text += f"   ~ BotX: {self.versions['BotX']} \n"
        log_text += f"   ~ PyroGram: {self.versions['pyrogram']} \n"
        log_text += f"   ~ Python: {self.versions['python']}"
        try:
            await self.BotX.send_photo(
                self.loggerID,
                "https://telegra.ph/file/3e28ce1ed1a89395ac07b.jpg",
                caption=log_text,
                parse_mode=ParseMode.MARKDOWN,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Start me", url=f"https://t.me/{self.BotX.me.username}?start=start"),
                        ],
                        [
                            InlineKeyboardButton("channel", url=f"https://t.me/{self.updateChannel}"),
                            InlineKeyboardButton("support", url=f"https://t.me/{self.supportGroup}"),
                        ],
                    ]
                ),
            )
        except Exception as e:
            self.logs.error(f"Error sending start message: {e}")

    async def reboot(self) -> None:
        try:
            await self.BotX.stop()
        except Exception as error:
            self.logs.info(str(error))

        await self.stopAllClients()

        args = [sys.executable, "-m", "BadX"]
        os.execl(sys.executable, *args)
        quit()

    async def help(self, chat_id: int) -> None:
        try:
            await self.BotX.send_photo(
                chat_id,
                self.logo,
                helpMessages.start.format(self.handler, self.updateChannel, self.supportGroup),
                reply_markup=help_buttons,
            )
        except Exception as er:
            await self.BotX.send_message(
                chat_id,
                f"**Error:** {str(er)} \n\n__Report in @{self.supportGroup}__"
            )

    async def loadPlugs(self) -> None:
        count = 0
        files = glob.glob("BadX/assistant/*.py")
        for file in files:
            with open(file) as f:
                path = Path(f.name)
                shortname = path.stem.replace(".py", "")
                if shortname.startswith("__"):
                    continue
                fpath = Path(f"BadX/assistant/{shortname}.py")
                name = "BadX.assistant." + shortname
                spec = importlib.util.spec_from_file_location(name, fpath)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["BadX.assistant." + shortname] = load
                count += 1
            f.close()
        LOGS.info(
            f"- > Loaded User Plugin: '{count}'"
        )

    async def startup(self) -> None:
        LOGS.info(
            f"-> Starting BotX ....."
        )
        await self.startBot()
        await self.StartAllClients()
        #await self.loadPlugs()
        await self.sudo.loadSudo()
        await self.restrict.loadRestrictChats()
        await self.startMessage()

TheBotX = BotX()
