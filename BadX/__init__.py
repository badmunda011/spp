import time

from platform import python_version

from BadX.functions.database import dataBase
from BadX.config import PING_MSG

from pyrogram import __version__


# --- start time --- #
StartTime = time.time()

# --- versions --- #
version = {
    "BadX": "v2.0",
    "pyrogram": __version__,
    "python": python_version(),
}

UpdateChannel = "HEROKUBIN_01"
SupportGroup = "ll_THE_BAD_BOT_ll"

activeTasks: dict = {}
dataBase = dataBase

#  --- etx
if PING_MSG:
    pingMSG = str(PING_MSG)
else:
    pingMSG = "BadX"