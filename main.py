from aiogram.utils import executor
import logging
from handlers.FSM import review_client, send_to_tg_channel

# ===========================================================================
from config import dp, bot, Admins
from handlers.commands import register_start
from handlers.FSM.FSM_all_products_cities import all_products
from keyboards import buttons
from config import data_b


# ==================================================================================================================
async def on_startup(_):
    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text="Бот запущен!", reply_markup=buttons.startForAdmins)
        await data_b.connect()


async def on_shutdown(_):
    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text="Бот отключен!", reply_markup=None)


# ==================================================================================================================

review_client.register_review(dp)
send_to_tg_channel.register_send_to_channel(dp)

all_products.register_all_products(dp)

register_start(dp)
# ===========================================================================
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
