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
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_all_handlers

# Import the database object from db.py
from db import db

#  LOGGING 
logging.basicConfig(level=logging.INFO)

#  WEB SERVER (FOR RAILWAY/RENDER FIX) 
# Railway usually provides a PORT variable automatically
PORT = int(os.environ.get("PORT", 8080))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Pikachuu Group Manager Bot is running")

def start_web_server():
    try:
        server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
        logging.info(f"Health check server running on port {PORT}")
        server.serve_forever()
    except Exception as e:
        logging.error(f"Web server failed: {e}")

# Start web server in background to prevent Railway from timing out
threading.Thread(target=start_web_server, daemon=True).start()

#  TELEGRAM BOT 
app = Client(
    "pikachuu_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register all moderation and welcome handlers
register_all_handlers(app)

if __name__ == "__main__":
    print("༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Bot is starting...")
    app.run()
