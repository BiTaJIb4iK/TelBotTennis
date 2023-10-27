import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, BotCommandScopeChat, CallbackQuery, ContentType, Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, MagicData, Filter
from aiogram.methods import set_my_commands
from aiogram.methods.set_my_commands import SetMyCommands
#from aiogram.types.bot_command_scope_default import BotCommandScopeDefault

from core.Handlers.main_menu import commandStartHandler, showDonate, showProfile, commandStartCallback, showSupport
from core.Handlers.selection import selectTime, selectCourt, selectDay, book
#from core.Middleware.middleware import SelectedCourtMiddleware#, SelectedDayMiddleware, SelectedTimeMiddleware
from core.Database.debug import clearTable, selectTable, printAllTables
from core.Database.basic import setUpDataBaseDefault
from core.Database.user import getUserBadges

TOKEN = "1448760736:AAFTlkLPGWrzSGyIwbaRh8PorgRFUJEoraA"

async def main() -> None:
    #Database section
    setUpDataBaseDefault()
    #Bot section
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    #Middleware 
    #dp.callback_query.middleware.register(SelectedCourtMiddleware())

    dp.message.register(commandStartHandler, CommandStart())

    #change_language;book;find_opponent;feedback

    dp.callback_query.register(commandStartCallback, F.data == "main_menu")

    dp.callback_query.register(selectCourt, F.data == "select_court")
    dp.callback_query.register(selectDay, F.data.contains("day"))
    dp.callback_query.register(selectTime,F.data.contains("time"))
    dp.callback_query.register(book, F.data.contains("book"))

    dp.callback_query.register(showProfile, F.data == "show_profile")
    dp.callback_query.register(showDonate, F.data == "donate")
    dp.callback_query.register(showSupport, F.data == "show_support")

    await dp.start_polling(bot)

def setUpLoggin():
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Set the root logger level to the lowest level you want to capture

    # Create a console handler and set the level
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # Set the console log level to INFO or any other desired level

    # Create a file handler and set the level
    file_handler = logging.FileHandler('app.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)  # Set the file log level to DEBUG or any other desired level

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Set the formatter for both handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

if __name__ == "__main__":
    setUpLoggin()
    asyncio.run(main())
    #printAllTables()