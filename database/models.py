from typing import Optional
from dataclasses import (
    dataclass, 
    field,
)
from datetime import (
    datetime, 
    timezone,
)

import constants


@dataclass
class User:
    """
    Represents a user in the system.

    Attributes:
        user_id: Telegram user ID.
        access_level: The user's access level. This is the value of the 
            UserAccessRoles enum, not the enum object itself. This approach is 
            used for compatibility with MongoDB, which does not support storing 
            enum types directly.
        created_at: Timestamp when the user was created (UTC).
        updated_at: Timestamp when the user was last updated (UTC).
    """
    user_id: int
    access_level: int = (
        constants.UserAccessRoles.USER
    )
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


# TODO: Documentation, auxiliary methods, refactoring.
@dataclass
class UserProfile:
    user_id: int
    race: str
    nickname: str 
    guild_name: str
    character_lvl: int
    paragon_lvl: int 
    max_hp: int 
    attack: int
    armor: int
    dodge: int
    crit: int
    accuracy: int
    character_exp: int
    adena: int

    updated_at: Optional[datetime] = None


@dataclass
class MediaCache:
    """
    Cache for Telegram media file ID.
    
    Attributes:
        cache_key: Unique key for the cached item.
        file_id: Telegram file identifier (file_id).
    """
    cache_key: str
    file_id: str
