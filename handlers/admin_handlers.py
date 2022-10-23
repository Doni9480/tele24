from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot_init import bot
from config import ID_LIST_ADMINS


# @dp.callback_query_handler()
async def callback(message: CallbackQuery):
    if message.data == 'settings':
        markap = InlineKeyboardMarkup()
        markap.insert(InlineKeyboardButton(text="Все команды", callback_data="sett_comsands"))
        markap.insert(InlineKeyboardButton(text="Уведомление", callback_data="sett_comsands2"))
        markap.insert(InlineKeyboardButton(text="Обнавления", callback_data="sett_comsands3"))
        markap.insert(InlineKeyboardButton(text="База Данных", callback_data="sett_comsands4"))
        markap.insert(InlineKeyboardButton(text="Ползователи", callback_data="sett_comsands5"))

        await bot.send_message(chat_id=ID_LIST_ADMINS[0], text="Настройки:", reply_markup=markap)
    elif message.data == 'sett_comsands':
        comm = """
        /menu - меню
        /start - старт
        /help - помощ
        /lents - лента новастей
        /section_news - разделы новостей"""
        await bot.send_message(chat_id=ID_LIST_ADMINS[0], text=f"Команды:{comm}")


def register_admin_message_handlers(dp: Dispatcher):
    lam = lambda message: 'settings' in message.data or 'sett' in message.data
    dp.register_callback_query_handler(callback, lam)


