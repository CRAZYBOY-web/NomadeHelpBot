# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# Modified/Maintained by: ⏤͟͟ 𝑪𝒓𝒂𝒛𝒚࿐𝑩𝒐𝒚 亗
#
# Support: https://t.me/+UhZo8ZsUECYyYWI1
# Channel: https://t.me/pikachuu_updates
#
# License: Custom Open-Source (Credits must remain; strictly no resale)
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    print("✅ Group commands registered!")

