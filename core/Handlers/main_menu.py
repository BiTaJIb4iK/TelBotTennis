import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, BotCommandScopeDefault, CallbackQuery, ContentType
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from datetime import datetime

from core.Keyboards.general import getMainMenuKeyboard, getProfileKeyboard
from core.Database.user import addUser, checkValidUser, getUser
from core.Database.debug import selectTable


async def commandStartHandler(message: types.Message) -> None:
    msg = f'Вітаю <b>{message.from_user.full_name}</b>!\nЦе демо версія боту для бронювання тенісних кортів по Києву. Якщо хочете додати корт до боту, пишіть у підтрику. Безкоштовний хостинг закінчується 15/11/23, якщо хочете підтримати розробку даного проекту натисніть відповідну кнопку. Бажаю вам приємного користування!'
    addUser(message.from_user.id, message.from_user.full_name)
    await message.answer(msg, reply_markup=getMainMenuKeyboard())



async def commandStartCallback(call: CallbackQuery, bot: Bot) -> None:
    msg = f'Вітаю <b>{call.from_user.full_name}</b>!\nЦе демо версія боту для бронювання тенісних кортів по Києву. Якщо хочете додати корт до боту, пишіть у підтрику. Безкоштовний хостинг закінчується 15/11/23, якщо хочете підтримати розробку даного проекту натисніть відповідну кнопку. Бажаю вам приємного користування!'
    addUser(call.from_user.id, call.from_user.full_name)
    await call.message.answer(msg, reply_markup=getMainMenuKeyboard())
    await call.answer()



async def showProfile(call: CallbackQuery, bot: Bot) -> None:
    if checkValidUser(call.from_user.id) is True:
        res = getUser(call.from_user.id)
        msg = f"Профіль\nІм'я : {res[1]}\nДата реєстрації : {res[2]}\nРейтинг : {res[3]}\nЗначок : {res[4]}(comming soon)\n"

        await call.message.answer(msg, reply_markup=getProfileKeyboard())

    else:
        #TODO add message to error database 
        logging.error(f"Error user_id is invalid, can't load profile error ID - INVALID_USER_ID : user_id - {call.from_user.id}, select result : {getUser(call.from_user.id)}")
        await call.message.answer(f"<b>Помилка відображення профілю, скопіюйте це повідомлення та напишіть в підтрику</b> : [user_id is invalid, can't load profile error ID - <b>INVALID_USER_ID</b> ]  {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}", parse_mode = ParseMode.HTML)

    await call.answer()
    



async def showDonate(call: CallbackQuery, bot: Bot) -> None:
    #await call.message.answer("Проект є абсолютно <b>безкоштовним</b> та підтримується лише розробником цього додатку. Ви можете підтримати розробку цього проету! Буду вдячний будь-якій сумі. Також підтвердивши платіж ви можете отримати винагороди у вигляді значків, розширеного функціоналу, можливість приймати участь у турнірах та інші. Усі можливості будуть підтверджені демократично за допомогою голосування.\nMonoBank : 000\nPrivatBank : 000\nЗавчасно дякую за внесок у розвиток проету!")
    await call.message.answer("""
Проект абсолютно <b>безкоштовний</b> та підтримується виключно розробником. Ваша підтримка дуже важлива для нас! 
Ми вдячні за будь-який внесок. Дякуємо тим, хто вже долучився до розвитку проекту.

Додатково, після підтвердження платежу ви отримаєте доступ до бонусів, таких як підвищення рейтингу, значки, розширений функціонал та можливість участі в турнірах.

Всі можливості будуть обиратися демократично за допомогою голосування.

Реквізити для підтримки:
MonoBank: <code>5375411426523267</code>
PrivatBank: <code>5168757424525881</code>

Віталій Б.

Дякуємо за вашу підтримку та внесок у розвиток проекту!
""")
    await call.answer()



async def showSupport(call: CallbackQuery, bot: Bot) -> None:
    await call.message.answer("Ви можете звернутися за допомогою в підтримку : (comming soon)")
    await call.answer()

