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
from dotenv import load_dotenv

# Load .env file if it exists (for local testing)
load_dotenv()

# --- Telegram API Config ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# --- Database Config ---
MONGO_URI = os.environ.get("MONGO_URI", "")
DB_NAME = os.environ.get("DB_NAME", "PikachuuDB")

# --- Owner and Bot Info ---
OWNER_ID = int(os.environ.get("OWNER_ID", 5000520402))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "PikachuuHelpBot")

# --- Custom Links & Visuals ---
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "https://t.me/+UhZo8ZsUECYyYWI1")
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/pikachuu_updates")
START_IMAGE = os.environ.get("START_IMAGE", "https://files.catbox.moe/9qftmz.jpg")

# Simple validation check
if not API_ID or not API_HASH or not BOT_TOKEN:
    print("⚠️ WARNING: API_ID, API_HASH, or BOT_TOKEN is missing in environment variables!")

if not MONGO_URI:
    print("⚠️ WARNING: MONGO_URI is missing! MongoDB features will not work.")
