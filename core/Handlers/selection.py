import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, BotCommandScopeDefault, CallbackQuery, ContentType
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from datetime import datetime
import random

from core.Keyboards.general import getMainMenuKeyboard
from core.Keyboards.BookSelection import getSelectCourtKeyboard, getSelectDayKeyboard, getSelectTimeKeyboard
from core.Database.user import addUser, checkValidUser, getUser
from core.Database.debug import selectTable
from core.DataTypes.dbtypes import BookingSelectionCallback
from core.Database.booking import getCourts, getDays, getTimesAvailable

async def selectCourt(call: CallbackQuery, bot: Bot) -> None:
    all_courts = getCourts()
    msg = "<b>Виберіть Корт : </b>\n"
    for court in all_courts:
        msg += str(court[0]+1) + ".\nНазва :  "+ court[1] + "\nОпис  :  " + court[2] +"\n\n"

    await call.message.answer(msg, reply_markup=getSelectCourtKeyboard(all_courts=all_courts), parse_mode=ParseMode.HTML)
    await call.answer()

async def selectDay(call: CallbackQuery, bot: Bot) -> None:
    all_days = getDays()
    msg = "<b>Виберіть День : </b>\n"

    await call.message.answer(msg, reply_markup=getSelectDayKeyboard(BookingSelectionCallback.unpack(call.data), all_days), parse_mode=ParseMode.HTML)

    await call.answer()

async def selectTime(call: CallbackQuery, bot: Bot) -> None:
    callBackData = BookingSelectionCallback.unpack(call.data)
    times = getTimesAvailable(date_id = callBackData.day)

    #show case taken spots

    await call.message.answer("Select Time : ", reply_markup=getSelectTimeKeyboard(callBackData, times), parse_mode=ParseMode.HTML)
    await call.answer()

async def book(call: CallbackQuery, bot: Bot) -> None:
    data = BookingSelectionCallback.unpack(call.data)
    await call.message.answer("Забронювати : " + str(data.court) + " - " + str(data.day) + " - " + str(data.time))
    await call.answer()

# async def confirm_book(call: CallbackQuery, bot: Bot) -> None:
#     data = BookingSelectionCallback.unpack(call.data)
#     await call.message.answer("", reply_markup=)
#     await call.answer()