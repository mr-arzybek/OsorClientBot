from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()


TOKEN = config('TOKEN')
Director = [5676759336, ]
CHANNEL_ID = int(config('CHANNEL_ID'))
Admins = [5676759336, ]

Manager = 5676759336
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

ip = config('ip')
PostgresUser = config('PostgresUser')
PostgresPassword = config('PostgresPassword')
DATABASE = config('DATABASE')

POSTGRES_URL = "postgresql://postgres:123@locallhost:5432/OSOR_DB"
data_b = Database(POSTGRES_URL)