import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
load_dotenv('.env')

app = Client("Имя | Бот",
             api_id=os.environ["API_ID"], api_hash=os.environ["API_HASH"], bot_token=os.environ['API_TOKEN'],
             in_memory=True)


@app.on_message(filters.command("all"))
@app.on_message(filters.command("start"))
async def get_chat_members(_, message: Message):
    if message.chat.type == ChatType.PRIVATE or message.text == '/start':
        return await message.reply('Привет это бот чтобы тегать всех usage: /all сейчас это не сработало тк. мы находимся в приватном чате или ты использовал start')

    chat_members = []
    me = await app.get_me()
    async for member in app.get_chat_members(message.chat.id):
        if member.user.username not in [me.username, os.environ.get('DONT_PING', '')]:
            chat_members.append("@" + member.user.username)
    try:
        await message.reply(' '.join(chat_members))
    except Exception as e:
        await message.reply('Сообщение вышло слишком длинным' + ' '.join(chat_members)[:2000])

app.run()
