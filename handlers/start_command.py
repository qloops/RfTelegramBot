from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram import (
    Client,
    filters,
)

from bot import bot
from keyboards import markup_keyboards
from database.utils import create_new_user
from constants.messages import BotMessages


@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id
    create_new_user.create_new_user(user_id=user_id)

    if message.chat.type == ChatType.PRIVATE:
        await message.reply(
            text=BotMessages.WELCOME, reply_markup=markup_keyboards.MENU_KEYBOARD
        )
    else:
        await message.reply(text=BotMessages.WELCOME)
