from aiogram.utils import executor
import logging
from config import dp, bot, Admins, Director
from handlers.start import register_start

# ===========================================================================
async def on_startup(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="Бот запущен!")
    # await bot.send_message(chat_id=Director[0], text="Бот запущен!", reply_markup=buttons.start_director_markup)


register_start(dp)

# ===========================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)