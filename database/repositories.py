import logging
from typing import (
    TYPE_CHECKING, 
    TypeVar,
)

from .base_repository import BaseRepository
from .models import (
    User, 
    UserProfile,
    MediaCache,
)

if TYPE_CHECKING:
    from .database import MongoDBInterface

T = TypeVar("T")

logger = logging.getLogger(__name__)


class UserRepository(BaseRepository[User]):
    COLLECTION_NAME = "users"
    
    def __init__(self, db_interface: "MongoDBInterface"):
        super().__init__(db_interface, self.COLLECTION_NAME, User)

class UserProfileRepository(BaseRepository[UserProfile]):
    COLLECTION_NAME = "users_profiles"
    
    def __init__(self, db_interface: "MongoDBInterface"):
        super().__init__(db_interface, self.COLLECTION_NAME, UserProfile)


class MediaCacheRepository(BaseRepository[MediaCache]):
    COLLECTION_NAME = "media_cache"
    
    def __init__(self, db_interface: "MongoDBInterface"):
        super().__init__(db_interface, self.COLLECTION_NAME, MediaCache)
