import asyncio

from dotenv import load_dotenv
from pyrogram import Client, filters
import os

from pyrogram.types import Message

load_dotenv('.env')

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
bot_token = os.environ['API_TOKEN']

app = Client("Имя | Бот", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)


@app.on_message(filters.command("all"))
async def get_chat_members(_, message: Message):
    chat_members = []
    async for member in app.get_chat_members(message.chat.id):
        if member.user.username not in ['my_tag_all_bot', os.environ['DONT_PING']]:
            chat_members += [member.user.username]
    await message.reply("@" + ' @'.join(chat_members))


async def main():
    await app.run()


# asyncio.run(main())

app.run()
