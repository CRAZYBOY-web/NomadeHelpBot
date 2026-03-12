from pyrogram import Client, filters
from pyrogram.types import Message
from db import get_welcome_message, get_welcome_status, set_welcome_status, set_welcome_message

# --- Automatic Welcome Logic ---
@Client.on_message(filters.new_chat_members)
async def welcome_handler(client, message: Message):
    if not await get_welcome_status(message.chat.id):
        return

    welcome_text = await get_welcome_message(message.chat.id)
    if not welcome_text:
        welcome_text = "Welcome {mention} to {title}!"

    for new_user in message.new_chat_members:
        text = welcome_text.format(
            id=new_user.id,
            first=new_user.first_name,
            mention=new_user.mention,
            title=message.chat.title
        )
        await message.reply_text(text)

# --- Automatic Goodbye Logic ---
@Client.on_message(filters.left_chat_member)
async def goodbye_handler(client, message: Message):
    await message.reply_text(f"Goodbye {message.left_chat_member.mention}! We will miss you.")

# --- Command: Toggle Welcome ---
@Client.on_message(filters.command("welcome") & filters.group)
async def toggle_welcome(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return
    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Usage: `/welcome on` or `/welcome off`")
        return
    status = args[1].lower() == "on"
    await set_welcome_status(message.chat.id, status)
    await message.reply_text(f"✅ Welcome messages {'enabled' if status else 'disabled'}!")

# --- Command: Set Welcome Text ---
@Client.on_message(filters.command("setwelcome") & filters.group)
async def set_welcome_cmd(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return
    if len(message.text.split()) < 2:
        await message.reply_text("Usage: `/setwelcome Welcome to the group {first}!`")
        return
    welcome_text = message.text.split(None, 1)[1]
    await set_welcome_message(message.chat.id, welcome_text)
    await message.reply_text("✅ Custom welcome message saved!")

def register_welcome_handlers(app):
    pass
