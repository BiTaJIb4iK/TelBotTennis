import asyncio
import logging
import sys
import random
from typing import List

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, BotCommandScopeDefault, CallbackQuery, ContentType
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.DataTypes.dbtypes import BookingSelectionCallback
from core.Database.booking import getCourts


def getMainMenuKeyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Профіль📄', callback_data='show_profile')
    keyboard_builder.button(text='Вибрати мову🌐(в розробці)', callback_data='change_language')
    keyboard_builder.button(text='Забронювати корт📆', callback_data='select_court')
    keyboard_builder.button(text='Знайти суперника 🤼(в розробці)', callback_data='find_opponent')
    keyboard_builder.button(text='Турніри 🏆(в розробці)', callback_data='find_opponent')
    keyboard_builder.button(text='💰 Підтримати проект 💰', callback_data='donate')
    keyboard_builder.button(text='Підтримка💬', callback_data='show_support')
    keyboard_builder.button(text='Відгук📊', callback_data='feedback')

    keyboard_builder.adjust(2,1,2,1,2)

    return keyboard_builder.as_markup()

def getProfileKeyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Змінити значок', callback_data='change_display_badge')
    keyboard_builder.button(text='Оновити ім\'я', callback_data='refresh_name')
    keyboard_builder.button(text='Головне меню', callback_data='main_menu')

    keyboard_builder.adjust(2,1)

    return keyboard_builder.as_markup()

def getBackToMainMenuKeyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Головне меню', callback_data='main_menu')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()

