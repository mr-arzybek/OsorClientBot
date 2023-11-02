from config import bot
from aiogram import types, Dispatcher


async def order(message: types.Message):
    await message.answer('dshfgsdufgdjdfkdfdf')



async def reservation(message: types.Message):
    await message.answer("gchjkfhgdfhfkjh")


async def try_on(message: types.Message):
    await message.answer("dfghfghtyyutj")


def register_order(dp: Dispatcher):
    dp.register_message_handler(order, commands=['заказать'])
    dp.register_message_handler(reservation, commands=['забронировать'])
    dp.register_message_handler(try_on, commands=['примерить'])