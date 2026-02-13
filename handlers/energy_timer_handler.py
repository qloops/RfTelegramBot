import re

from pyrogram.types import Message
from pyrogram import (
    Client,
    filters,
)

import rules
from bot import bot
from views.formatters import EnergyFormatter
from constants.patterns import ENERGY_MAIN_VALIDATOR
from utils import convert_to_utc


@bot.on_message(
    rules.game_bot_forwarded & filters.regex(re.compile(ENERGY_MAIN_VALIDATOR))
)
async def energy_timer_handler(client: Client, message: Message):
    date = convert_to_utc(message.forward_date)
    energy = int(message.matches[0].group("energy"))

    await message.reply(text=EnergyFormatter.format(energy=energy, forward_date=date))
