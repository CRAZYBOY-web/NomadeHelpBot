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
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')

# --- MONGODB CONNECTION ---
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# ==========================================================
# 🟢 WELCOME & USER SYSTEM
# ==========================================================

async def add_user(user_id, first_name):
    await db.users.update_one({"user_id": user_id}, {"$set": {"first_name": first_name}}, upsert=True)

async def get_all_users():
    cursor = db.users.find({}, {"_id": 0, "user_id": 1})
    return [doc["user_id"] async for doc in cursor if "user_id" in doc]

async def set_welcome_message(chat_id, text: str):
    await db.welcome.update_one({"chat_id": chat_id}, {"$set": {"message": text}}, upsert=True)

async def get_welcome_message(chat_id):
    data = await db.welcome.find_one({"chat_id": chat_id})
    return data.get("message") if data else None

# ==========================================================
# 🛡️ ANTI-LINK & APPROVAL SYSTEM
# ==========================================================

async def set_antilink(chat_id, status: bool):
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"antilink": status}}, upsert=True)

async def get_antilink(chat_id):
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("antilink", False) if data else False

async def set_approval(chat_id, status: bool):
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"approval": status}}, upsert=True)

async def get_approval(chat_id):
    data = await db.settings.find_one({"chat_id": chat_id})
    return data.get("approval", False) if data else False

# ==========================================================
# ⚠️ WARN & LOCK SYSTEM
# ==========================================================

async def add_warn(chat_id: int, user_id: int) -> int:
    data = await db.warns.find_one({"chat_id": chat_id, "user_id": user_id})
    warns = data.get("count", 0) + 1 if data else 1
    await db.warns.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"count": warns}}, upsert=True)
    return warns

async def get_warns(chat_id: int, user_id: int) -> int:
    data = await db.warns.find_one({"chat_id": chat_id, "user_id": user_id})
    return data.get("count", 0) if data else 0

async def reset_warns(chat_id: int, user_id: int):
    await db.warns.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"count": 0}}, upsert=True)

async def set_lock(chat_id, lock_type, status: bool):
    await db.locks.update_one({"chat_id": chat_id}, {"$set": {f"locks.{lock_type}": status}}, upsert=True)

async def get_locks(chat_id):
    data = await db.locks.find_one({"chat_id": chat_id})
    return data.get("locks", {}) if data else {}
