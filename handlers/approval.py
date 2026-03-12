from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from db import get_approval

def register_approval_handlers(app):
    pass
@Client.on_chat_join_request()
async def approval_handler(client, request: ChatJoinRequest):
    chat_id = request.chat.id
    
    # Check if Auto-Approval is ON for this chat
    if await get_approval(chat_id):
        try:
            await client.approve_chat_join_request(chat_id, request.from_user.id)
            # Optional: Send a private message to the user
            await client.send_message(
                request.from_user.id, 
                f"✅ Your request to join **{request.chat.title}** has been approved!"
            )
        except Exception as e:
            print(f"Approval Error: {e}")

def register_approval_handlers(app):
    pass
