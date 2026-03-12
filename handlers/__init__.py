# ============================================================
# ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Group Manager Bot
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands
from .welcome import register_welcome_handlers
from .moderation import register_moderation_handlers
from .approval import register_approval_handlers

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    register_welcome_handlers(app)
    register_moderation_handlers(app)
    register_approval_handlers(app)
    
    print("✅ ༒ ᴘɪᴋᴀᴄʜᴜᴜ ༒ Systems are all Online!")
