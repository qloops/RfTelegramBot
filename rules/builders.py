from pyrogram.types import (
    Message,
    InlineQuery
)
from pyrogram import filters

from database import db_interface
from constants.roles import UserAccessRoles
from utils.access_check import access_check

def create_forwarded_from_filter(user_id: int):
    async def func(_, __, query: Message):
        return query.forward_from and query.forward_from.id == user_id
    
    return filters.create(func)


def create_empty_profile_filter():
    async def func(_, __, query: Message | InlineQuery):
        return not db_interface.users_profiles.exists(
            condition={"user_id": query.from_user.id}
        )

    return filters.create(func)


def create_is_user_admin_filter():
    async def func(_, __, query: Message | InlineQuery):
        user = db_interface.users.find_one(
            condition={"user_id": query.from_user.id}
        )
        if user:
            return access_check(
                user.access_level,
                UserAccessRoles.ADMINISTRATOR
            )

    return filters.create(func)
