import asyncio
import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

load_dotenv(".env")

app = Client(
    "Имя | Бот",
    api_id=os.environ["API_ID"],
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["API_TOKEN"],
    in_memory=True,
)


@app.on_message(filters.command("all"))
@app.on_message(filters.command("start"))
async def get_chat_members(_, message: Message):
    if message.chat.type == ChatType.PRIVATE or message.text == "/start":
        return await message.reply(
            "Привет это бот чтобы тегать всех usage: /all сейчас это не сработало тк. мы находимся в приватном чате или ты использовал start"
        )

    members = app.get_chat_members(message.chat.id)
    if not members:
        return await message.reply("Нет доступа к участникам чата")

    chat_members = ""

    async for member in members:
        if member.user and member.user.username:
            chat_members += f"@{member.user.username} \n"

        if len(chat_members) > 3000:
            await message.reply(chat_members)
            chat_members = ""
            await asyncio.sleep(5)


app.run()
