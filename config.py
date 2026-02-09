import os
import logging
import logs
from dotenv import load_dotenv

load_dotenv()

c_level_str = os.getenv("CONSOLE_LOG_LEVEL", "ERROR").upper()
f_level_str = os.getenv("FILE_LOG_LEVEL", "INFO").upper()

CONSOLE_LOG_LEVEL = getattr(logging, c_level_str, logging.ERROR)
FILE_LOG_LEVEL = getattr(logging, f_level_str, logging.INFO)

logs.configure_logging(console_level=CONSOLE_LOG_LEVEL, file_level=FILE_LOG_LEVEL)

logger = logging.getLogger(__name__)

if (API_ID := os.getenv("API_ID")) is None:
    logger.error("The API_ID must not be empty.")
    raise EnvironmentError("API_ID is missing in .env file")

if (API_HASH := os.getenv("API_HASH")) is None:
    logger.error("The API_HASH must not be empty.")
    raise EnvironmentError("API_HASH is missing in .env file")

if (BOT_TOKEN := os.getenv("BOT_TOKEN")) is None:
    logger.error("The BOT_TOKEN must not be empty.")
    raise EnvironmentError("BOT_TOKEN is missing in .env file")

if (raw_game_id := os.getenv("BOT_GAME_ID")) is None:
    logger.error("The BOT_GAME_ID must not be empty.")
    raise EnvironmentError("BOT_GAME_ID is missing in .env file")

try:
    BOT_GAME_ID = int(raw_game_id)
except ValueError:
    logger.error(f"The BOT_GAME_ID must be a valid integer, got: {raw_game_id}.")
    raise ValueError(f"Invalid BOT_GAME_ID format")

DB_NAME = os.getenv("DB_NAME", "rf_bot_db")
DB_HOST = os.getenv("DB_HOST", "localhost")

try:
    DB_PORT = int(os.getenv("DB_PORT", 27017))
except ValueError:
    logger.warning("Invalid DB_PORT, using default 27017.")
    DB_PORT = 27017
