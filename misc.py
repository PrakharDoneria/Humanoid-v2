# Logging
import logging

try:
    from aiogram import Bot, Dispatcher, types
    from config import token
except ImportError as e:
    logging.error("Failed to import required modules: %s", e)
    # You may want to handle this error further, such as exiting the script or raising an exception

logging.basicConfig(level=logging.INFO)

# Bot configs
try:
    bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)
except Exception as e:
    logging.error("Failed to initialize bot: %s", e)
    # Handle initialization failure, like exiting the script or logging an error
