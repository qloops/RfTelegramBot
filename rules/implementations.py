import config
from .builders import (
    create_forwarded_from_filter,
    create_empty_profile_filter,
    create_is_user_admin_filter,
)


class GameBotForwarded:
    BOT_GAME_ID = config.BOT_GAME_ID

    def __new__(cls):
        return create_forwarded_from_filter(cls.BOT_GAME_ID)


class EmptyProfle:
    def __new__(cls):
        return create_empty_profile_filter()


class UserAdmin:
    def __new__(cls):
        return create_is_user_admin_filter()
