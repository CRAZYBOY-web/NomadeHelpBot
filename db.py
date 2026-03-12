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
logging.basicConfig(
    level=logging.INFO, 
    format='[%(levelname)s] %(asctime)s - %(message)s'
)

# --- MONGODB CONNECTION ---

# Check if MONGO_URI is valid before initializing the client
if not MONGO_URI or MONGO_URI.strip() == "":
    logging.error("❌ MONGO_URI is missing! MongoDB features will be disabled.")
    client = None
    db = None
else:
    try:
        # Initialize the Async client
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        logging.info("✅ MongoDB connected successfully!")
    except Exception as e:
        logging.error(f"❌ Failed to connect to MongoDB: {e}")
        client = None
        db = None

# ==========================================================
# 🟢 HELPER FUNCTIONS (Safe from NoneType errors)
# ==========================================================

async def add_user(user_id, first_name):
    if db is None: return
    await db.users.update_one({"user_id": user_id}, {"$set": {"first_name": first_name}}, upsert=True)

async def set_welcome_status(chat_id, status: bool):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"welcome_enabled": status}}, upsert=True)

async def get_welcome_status(chat_id) -> bool:
    if db is None: return False
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("welcome_enabled", False) if data else False

async def set_welcome_message(chat_id, text: str):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"welcome_text": text}}, upsert=True)

async def get_welcome_message(chat_id):
    if db is None: return None
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("welcome_text") if data else None

# --- Anti-Link & Approval ---

async def set_antilink(chat_id, status: bool):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"antilink": status}}, upsert=True)

async def get_antilink(chat_id):
    if db is None: return False
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("antilink", False) if data else False

async def set_approval(chat_id, status: bool):
    if db is None: return
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"approval": status}}, upsert=True)

async def get_approval(chat_id):
    if db is None: return False
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("approval", False) if data else False
