from .implementations import (
    GameBotForwarded,
    EmptyProfle,
    UserAdmin,
)

__all__ = [
    "game_bot_forwarded", 
    "empty_profle",
    "is_user_admin",

]
game_bot_forwarded = GameBotForwarded()
empty_profle = EmptyProfle()
is_user_admin = UserAdmin()
