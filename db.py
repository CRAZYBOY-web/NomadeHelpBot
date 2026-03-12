# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# Modified/Maintained by: ⏤͟͟ 𝑪𝒓𝒂𝒛𝒚࿐𝑩𝒐𝒚 亗
#
# Support: https://t.me/+UhZo8ZsUECYyYWI1
# Channel: https://t.me/pikachuu_updates
#
# License: Custom Open-Source (Credits must remain; strictly no resale)
# ============================================================

import motor.motor_asyncio
from config import MONGO_URI, DB_NAME
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# --- THE FIX: Initialize as None ---
db = None

if not MONGO_URI or not str(MONGO_URI).strip():
    logging.error("❌ MONGO_URI is missing! MongoDB features will be disabled.")
else:
    try:
        # We only create the client if the URI actually looks like a link
        if "mongodb" in str(MONGO_URI):
            client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
            db = client[DB_NAME]
            logging.info("✅ MongoDB connection initialized.")
        else:
            logging.error("❌ MONGO_URI is not a valid MongoDB link!")
    except Exception as e:
        logging.error(f"❌ MongoDB Error: {e}")

# ==========================================================
# 🟢 HELPERS WITH SAFETY CHECKS
# ==========================================================

async def get_welcome_status(chat_id):
    if db is None: return False # Prevents crash if DB is offline
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("welcome_enabled", False) if data else False

async def set_welcome_status(chat_id, status: bool):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"welcome_enabled": status}}, upsert=True)

async def get_welcome_message(chat_id):
    if db is None: return None
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("welcome_text") if data else None

async def set_welcome_message(chat_id, text: str):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"welcome_text": text}}, upsert=True)

async def get_antilink(chat_id):
    if db is None: return False
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("antilink", False) if data else False

async def get_approval(chat_id):
    if db is None: return False
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("approval", False) if data else False

async def set_approval(chat_id, status: bool):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"approval": status}}, upsert=True)
