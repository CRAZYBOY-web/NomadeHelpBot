# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# Modified/Maintained by: ⏤͟͟ 𝑪𝒓𝒂𝒛𝒚࿐𝑩𝒐𝒚 亗
#
# Support: https://t.me/+UhZo8ZsUECYyYWI1
# Channel: https://t.me/pikachuu_updates
#
# License: Custom Open-Source (Credits must remain; strictly no resale)
# ============================================================

import os
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client

# 1. IMPORT THESE FIRST
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_all_handlers
from db import db

# 2. NOW YOU CAN RUN THE CHECK
if __name__ == "__main__":
    if not API_ID or not API_HASH or not BOT_TOKEN:
        print("❌ CRITICAL ERROR: API_ID, API_HASH, or BOT_TOKEN is missing!")
        # We don't exit here so the web server can still respond to Railway
    
    # Rest of your start logic...
    print("༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Bot is starting...")
    
    app = Client(
        "pikachuu_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    register_all_handlers(app)
    app.run()
