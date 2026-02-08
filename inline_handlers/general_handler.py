from pyrogram import (
    Client,
    filters,
)
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQuery,
)

from bot import bot
from database import db_interface
from keyboards import markup_buttons
from views.formatters import UserProfileFormatter
from constants.messages import BotMessages


# It would be nice to make a less generic handler for the profile, but I'm just
# too lazy right now.
@bot.on_inline_query(filters.create(lambda _, __, query: not query.query))
async def _(client: Client, inline_query: InlineQuery):
    user_id = inline_query.from_user.id
    text = ""

    if db_interface.users_profiles.exists(condition={"user_id": user_id}):
        text = UserProfileFormatter.format(
            db_interface.users_profiles.find_one(condition={"user_id": user_id})
        )
    else:
        text = BotMessages.PROFILE_NOT_FOUND

    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title=markup_buttons.PROFILE_BUTTON,
                input_message_content=InputTextMessageContent(message_text=text),
                description=BotMessages.IM_BTN_SEND_PROFILE,
            )
        ],
        cache_time=0,
    )
