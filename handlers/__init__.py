# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands
from .welcome import register_welcome_handlers  # <--- Added this

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    register_welcome_handlers(app) # <--- Added this
    print("✅ All handlers (Start, Group, Welcome) registered!")
