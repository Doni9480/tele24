from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import link

from bot_init import bot
from web_parser import AlaToo24


async def menu(message: Message):
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="Лента новостей", callback_data='news_lent'))
    markup.insert(InlineKeyboardButton(text="Разделы", callback_data='news_section'))
    markup.insert(InlineKeyboardButton(text="Вчерашние", callback_data='news_lent_yesterday'))
    markup.insert(InlineKeyboardButton(text="Настройки", callback_data='news_user_settings'))
    await message.answer(text=f"Меню", reply_markup=markup)


async def options(message: CallbackQuery):
    if 'news_lent' in message.data:
        if not "news_lent_yesterday":
            f = 0
        else:
            f = 1
        lents = AlaToo24().news_lents()
        list_text = ""
        list_text += f'{list(lents.keys())[f]}\n'
        for dic in lents.get(list(lents.keys())[f]):
            text_link = link(title=dic.get("title"), url=dic.get("link"))
            list_text += f'{dic.get("time")}\n{text_link}\n\n'
        await bot.send_message(chat_id=message.message.chat.id, text=list_text, parse_mode='MarkdownV2')
    elif message.data == 'news_section':
        markup = InlineKeyboardMarkup()
        get_s = AlaToo24().news_sections()
        for name, l in get_s.items():
            markup.insert(InlineKeyboardButton(text=f"{name}", url=f"{l}"))
        await bot.send_message(chat_id=message.message.chat.id, text='Разделы:', reply_markup=markup)
    elif message.data == 'news_user_settings':
        await message.answer('В разработке!')


def register_client_message_handlers(dp: Dispatcher):
    # list_options = ['news_lent', 'news_section', 'news_date', 'news_user_settings']
    dp.register_message_handler(menu, lambda message: 'menu' in message.text)
    # callback handler
    dp.register_callback_query_handler(options, lambda message: 'news_' in message.data)
