from pyrogram import Client, filters
from pyrogram.types import Message
from db import set_welcome_status, set_welcome_message

def register_welcome_handlers(app):
    # This remains empty because we use decorators (@Client.on_message)
    # But it MUST exist so __init__.py doesn't crash the bot.
    pass
# --- Command: Toggle Welcome On/Off ---
@Client.on_message(filters.command("welcome") & filters.group)
async def toggle_welcome(client, message: Message):
    # Admin Check
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return

    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Usage: `/welcome on` or `/welcome off`")
        return

    status = args[1].lower()
    if status == "on":
        await set_welcome_status(message.chat.id, True)
        await message.reply_text("✅ Welcome messages enabled!")
    elif status == "off":
        await set_welcome_status(message.chat.id, False)
        await message.reply_text("❌ Welcome messages disabled!")

# --- Command: Set Custom Welcome Text ---
@Client.on_message(filters.command("setwelcome") & filters.group)
async def set_welcome_cmd(client, message: Message):
    # Admin Check
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return

    if len(message.text.split()) < 2:
        await message.reply_text(
            "Please provide a welcome message!\n\n"
            "**Placeholders:**\n"
            "{mention} - Mentions the user\n"
            "{title} - Group Name\n"
            "{first} - User's First Name"
        )
        return

    welcome_text = message.text.split(None, 1)[1]
    await set_welcome_message(message.chat.id, welcome_text)
    await message.reply_text("✅ Custom welcome message saved!")
