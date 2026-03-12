============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# Modified/Maintained by: ⏤͟͟ 𝑪𝒓𝒂𝒛𝒚࿐𝑩𝒐𝒚 亗
#
# Support: https://t.me/+UhZo8ZsUECYyYWI1
# Channel: https://t.me/pikachuu_updates
#
# License: Custom Open-Source (Credits must remain; strictly no resale)
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from db import get_antilink, set_antilink

# --- 1. ANTI-LINK SYSTEM ---
@Client.on_message(filters.group & ~filters.service, group=-1)
async def antilink_handler(client, message: Message):
    if not message.text or not await get_antilink(message.chat.id):
        return
    
    # Check for links
    if "t.me/" in message.text or "http" in message.text:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in ["administrator", "creator"]:
            try:
                await message.delete()
            except Exception:
                pass

@Client.on_message(filters.command("antilink") & filters.group)
async def toggle_antilink(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return

    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Usage: `/antilink on` or `/antilink off`")
        return

    status = args[1].lower() == "on"
    await set_antilink(message.chat.id, status)
    await message.reply_text(f"🚫 **Anti-Link** is now {'Enabled' if status else 'Disabled'}!")

# --- 2. BAN / KICK / MUTE SYSTEM ---

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return
    
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to ban them.")
    
    await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_text(f"✅ {message.reply_to_message.from_user.first_name} has been banned.")

@Client.on_message(filters.command("kick") & filters.group)
async def kick_user(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return
    
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to kick them.")
    
    await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_text(f"👞 {message.reply_to_message.from_user.first_name} has been kicked.")

# --- HANDLER REGISTRATION ---
def register_moderation_handlers(app):
    # Handlers are registered via decorators
    pass
