import re
from typing import Union
from datetime import (
    datetime,
    timedelta,
    timezone,
)

from pyrogram.types import Message
from pyrogram import (
    Client,
    filters,
)

import rules
from bot import bot
from views.formatters import UserProfileFormatter
from constants.messages import BotMessages
from constants.patterns import PROFILE_MAIN_VALIDATOR
from database import db_interface, models, utils
from utils import (
    ProfileParser,
    convert_to_utc,
)

UPDATE_TIME_LIMIT = 60


async def _validate_profile(
    message: Message,
    parsed_profile: models.UserProfile,
) -> Union[str, bool]:
    time_limit = timedelta(seconds=UPDATE_TIME_LIMIT)
    user_id = message.from_user.id

    if datetime.now(timezone.utc) - parsed_profile.updated_at > time_limit:
        return BotMessages.PROFILE_EXPIRED

    if parsed_profile.user_id != user_id:
        return BotMessages.NOT_YOUR_PROFILE

    return False


@bot.on_message(
    rules.game_bot_forwarded
    & filters.regex(re.compile(PROFILE_MAIN_VALIDATOR, re.DOTALL))
)
async def profile_handler(client: Client, message: Message):
    user_id = message.from_user.id
    parser = ProfileParser(message.text)
    game_profile = parser.parse()
    game_profile.updated_at = convert_to_utc(message.forward_date)

    utils.create_new_user.create_new_user(user_id=user_id)

    if error_msg := (await _validate_profile(message, game_profile)):
        await message.reply(text=error_msg)
        return

    old_profile = db_interface.users_profiles.find_one({"user_id": user_id})

    if old_profile:
        db_interface.users_profiles.update_one({"user_id": user_id}, game_profile)
    else:
        db_interface.users_profiles.insert_one(record=game_profile)

    response_text = UserProfileFormatter.format(
        profile=game_profile, old_profile=old_profile
    )

    await message.reply(text=response_text)
