from aiogram.utils import executor
import logging
from config import dp, bot, Admins
from handlers.commands import register_start
from handlers.FSM.review_client import register_review
from keyboards import buttons

# ==================================================================================================================
async def on_startup(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="Бот запущен!", reply_markup=buttons.start)
    # await bot.send_message(chat_id=Director[0], text="Бот запущен!", reply_markup=buttons.start_director_markup)


async def on_shutdown(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="Бот отключен!", reply_markup=None)
# ==================================================================================================================
register_start(dp)

register_review(dp)

# ===========================================================================
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
