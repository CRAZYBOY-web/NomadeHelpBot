# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# Modified/Maintained by: ⏤͟͟ 𝑪𝒓𝒂𝒛𝒚࿐𝑩𝒐𝒚 亗
#
# Support: https://t.me/+UhZo8ZsUECYyYWI1
# Channel: https://t.me/pikachuu_updates
#
# License: Custom Open-Source (Credits must remain; strictly no resale)
# ============================================================

# ... (your existing imports)

if __name__ == "__main__":
    # Internal check to ensure basic config is present
    if not API_ID or not API_HASH or not BOT_TOKEN:
        print("❌ CRITICAL ERROR: API_ID, API_HASH, or BOT_TOKEN is missing!")
        exit(1)

    print("༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Bot is starting...")
    
    # Check if DB is connected (Optional but helpful for debugging)
    if db is None:
        print("⚠️ WARNING: Bot is starting in OFFLINE mode (No Database).")
    else:
        print("✅ Database connection detected.")

    app.run()
