from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = config('TOKEN')
<<<<<<< HEAD

Admins = [908379438]

Director = [1738805992, ]
=======
CHANNEL_ID = int(config('CHANNEL_ID'))

Admins = [995712956, 908379438]

# Director = [1738805992, ]
>>>>>>> 506a49e5f92c438bf38702a0d26fca668305c158
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)