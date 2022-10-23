from aiogram import Dispatcher
from aiogram.types import Message
from write_read import WriteRead


async def welcome_user(message: Message):
    if message.text == '/start':
        rez = WriteRead().check_user_id(message.chat.id)
        if rez:
            new_dic = {**rez,message.from_user.first_name: message.chat.id}
            WriteRead().read_write_json_file(mod='w',data_for_write=new_dic)
        await message.answer(text=f'Добро пожаловать {message.from_user.first_name}!\n (Помощ - /help)')
    elif message.text == '/help':
        await message.answer(text=f"/menu <-- Меню\n")


def register_other_message_handlers(dp: Dispatcher):
    # list_options = ['news_lent', 'news_section', 'news_date', 'news_user_settings']
    dp.register_message_handler(welcome_user, lambda message: message.text in ['/start', '/help'])
