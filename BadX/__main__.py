from pyrogram import idle
from BadX.functions.clients import TheBadX

async def main():
    await TheBadX.startup()
    TheBadX.logs.info("-- BadX started --")
    await idle()
    await TheBadX.BadX.stop()
    await TheBadX.stopAllClients()

if __name__ == "__main__":
    TheBadX.run(main())