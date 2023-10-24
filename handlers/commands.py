from aiogram import types, Dispatcher
from keyboards import buttons


async def start_command(message: types.Message):
    await message.answer("Здравствуйте! Добро пожаловать в наш магазин модной одежды"
                         ", и я здесь, чтобы сделать ваше шопинг-путешествие незабываемым."
                         "С моей помощью вы сможете легко и удобно находить и выбирать стильные наряды. "
                         "Я предоставлю вам информацию о последних трендах, лучшие предложения и советы по стилю."
                         "Не стесняйтесь задавать мне вопросы, и я всегда готов помочь вам с выбором. Давайте начнем, "
                         "что вас интересует сегодня?", reply_markup=buttons.start)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])