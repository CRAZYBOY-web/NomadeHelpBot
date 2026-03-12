from pyrogram import Client, filters
from pyrogram.types import Message
from db import get_antilink, set_antilink

def register_moderation_handlers(app):
    pass
    
@Client.on_message(filters.group & ~filters.service, group=-1)
async def antilink_handler(client, message: Message):
    if not message.text or not await get_antilink(message.chat.id):
        return
    if "t.me/" in message.text or "http" in message.text:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in ["administrator", "creator"]:
            await message.delete()

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"] and message.reply_to_message:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply_text("✅ Banned!")

def register_moderation_handlers(app):
    pass # Decorators handle this
