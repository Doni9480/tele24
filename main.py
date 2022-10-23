from aiogram import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from web_parser import AlaToo24
# import s

from bot_init import dp, bot
from config import ID_LIST_ADMINS
from handlers.admin_handlers import register_admin_message_handlers
from handlers.clients_handlers import register_client_message_handlers
from handlers.other_handlers import register_other_message_handlers
from write_read import WriteRead

register_admin_message_handlers(dp)
register_client_message_handlers(dp)
register_other_message_handlers(dp)


async def on_startup(_):
    print('DONE!')
    for admin in ID_LIST_ADMINS:
        markup = InlineKeyboardMarkup()
        markup.insert(InlineKeyboardButton(text='Settings', callback_data='settings'))
        await bot.send_message(chat_id=admin, text='Бот функционирует!', reply_markup=markup)


async def update(time):
    while True:
        await asyncio.sleep(time)
        new_data = AlaToo24(work=True).get_html()



def main():
    loop = asyncio.get_event_loop()
    loop.create_task(update(600))
    executor.start_polling(dispatcher=dp, on_startup=on_startup)




if __name__ == '__main__':
    main()
