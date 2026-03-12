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

# Telegram API Config
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Database Config
MONGO_URI = os.environ.get("MONGO_URI", "")
DB_NAME = os.environ.get("DB_NAME", "PikachuuDB")

# Owner and Bot Details
OWNER_ID = int(os.environ.get("OWNER_ID", 5000520402))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "PikachuuX_Bot")

# Support & Updates
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "https://t.me/+UhZo8ZsUECYyYWI1")
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/pikachuu_updates")
START_IMAGE = os.environ.get("START_IMAGE", "https://files.catbox.moe/9qftmz.jpg")
