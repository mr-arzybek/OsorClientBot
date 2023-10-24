from aiogram.utils import executor
import logging
<<<<<<< HEAD
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
=======
from config import dp, bot, Admins
from handlers import commands
from handlers.FSM import review_client, send_to_tg_channel


# ===========================================================================
async def on_startup(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="Бот запущен!")
    # await bot.send_message(chat_id=Director[0], text="Бот запущен!", reply_markup=buttons.start_director_markup)


commands.register_start(dp)

review_client.register_review(dp)
send_to_tg_channel.register_send_to_channel(dp)

# ===========================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
>>>>>>> 506a49e5f92c438bf38702a0d26fca668305c158
