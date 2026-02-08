from pyrogram.types import Message
from pyrogram import (
    Client,
    filters,
)

from bot import bot
from keyboards import markup_buttons
from database import db_interface
from views.formatters import UserProfileFormatter
from constants.messages import BotMessages


@bot.on_message(
    filters.regex(f"^{markup_buttons.PROFILE_BUTTON}$") | filters.command("me")
)
async def profile_command(client: Client, message: Message):
    user_id = message.from_user.id
    user_profile = db_interface.users_profiles.find_one(condition={"user_id": user_id})

    if not user_profile:
        await message.reply(text=BotMessages.PROFILE_NOT_FOUND)
    else:
        await message.reply(text=UserProfileFormatter.format(user_profile))
