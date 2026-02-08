from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from . import markup_buttons

MENU_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=markup_buttons.PROFILE_BUTTON)]],
    resize_keyboard=True,
)
