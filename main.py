import os

from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv(".env")
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
hello_msg = (
    "Привет. Чтобы начать скачивание, скидывай сообщения с медиафайлами. По умолчанию они скачиваются в корневую "
    "папку. Чтобы изменить папку, просто напиши название новой папки. Все последующие файлы будут качаться в неё. "
    "Если хочешь качать снова в корень, то просто отправь / . По окончанию скачивания какого-то видео или фото, "
    "бот уведомит, что он закончил "
)
app = Client("Downloader", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

folder_name = ""


@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply(hello_msg)


@app.on_message(filters.text & filters.private)
async def get_folder_name(client, message):
    global folder_name
    folder_name = folder_name.join(message.text)
    await message.reply(f"Папка теперь '{folder_name}'")


@app.on_message(filters.media)
async def handle_media(client, message):
    message.status = "Готово"
    await client.download_media(message, file_name=f"D:/Downloads/{folder_name}/")
    await message.reply(message.status, "Готово")


app.run()
