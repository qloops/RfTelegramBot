import logging
import sys
import os
from logging.handlers import RotatingFileHandler


def configure_logging(console_level=logging.INFO, file_level=logging.ERROR):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s.%(funcName)s(%(lineno)d) - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(log_dir, "bot.log")

    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"  # 10MB
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logging.getLogger("pymongo").setLevel(logging.ERROR)
    logging.getLogger("pyrogram").setLevel(logging.ERROR)
    logging.getLogger("asyncio").setLevel(logging.ERROR)
