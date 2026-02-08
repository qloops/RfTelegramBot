import logging
from importlib.metadata import version

from pyrogram import idle

import config
import handlers
import inline_handlers
from bot import bot

logger = logging.getLogger(__name__)
__version__ = version("rf-telegram-bot")


async def main():
    try:
        await bot.start()
        logger.info(f"Bot @{bot.me.username} V{__version__} started!")
        await idle()
    except Exception as e:
        logger.error(f"Bot crashed: {e}.")
        raise
    finally:
        await bot.stop()
        logger.info("Bot stopped.")


if __name__ == "__main__":
    bot.run(main())
