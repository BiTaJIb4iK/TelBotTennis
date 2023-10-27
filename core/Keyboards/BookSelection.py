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


def getSelectCourtKeyboard(all_courts):
    keyboard_builder = InlineKeyboardBuilder()

    #pack Buttons
    for court in all_courts:
        keyboard_builder.button(text=court[1], callback_data=BookingSelectionCallback(state='day', court=court[0], day=-1, time=-1).pack())

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def getSelectDayKeyboard(data: BookingSelectionCallback, days):
    keyboard_builder = InlineKeyboardBuilder()

    for day in days:
        keyboard_builder.button(text=day[1], callback_data=BookingSelectionCallback(state='time', court=data.court, day=day[0], time=-1).pack())

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def getSelectTimeKeyboard(data: BookingSelectionCallback, times):
    keyboard_builder = InlineKeyboardBuilder()

    for time in times:
        keyboard_builder.button(text=time[1], callback_data=BookingSelectionCallback(state='book', court=data.court, day=data.day, time=time[0]).pack())

    keyboard_builder.adjust(3)

    return keyboard_builder.as_markup()
