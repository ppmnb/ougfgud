from telethon.sync import TelegramClient

from telethon.sessions import StringSession

import os

APP_ID = input("APP_id : ")

APP_HASH = input("APP_Hash : ")

BOT_USERNAME = input("uesrnembot : ")

session = input("T : ")

SESSION = input("T :")

token = input("BOT TO : ")

APP_ID1 = APP_ID

APP_HASH1 = APP_HASH

BOT_USERNAME1 = BOT_USERNAME

session1 = session

SESSION1 = SESSION

token1 = token

fifthon = TelegramClient(StringSession(session1), APP_ID1, APP_HASH1)

bot = TelegramClient("bot", APP_ID1, APP_HASH1).start(bot_token=token1)

ispay = ['yes']

ispay2 = ['yes']

print(token1)

bot.start()
