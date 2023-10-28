from aiogram import types, Dispatcher
from keyboards import buttons


async def start_command(message: types.Message):
    await message.answer("Здравствуйте! Добро пожаловать в наш магазин модной одежды"
                         ", и я здесь, чтобы сделать ваше шопинг-путешествие незабываемым."
                         "С моей помощью вы сможете легко и удобно находить и выбирать стильные наряды. "
                         "Я предоставлю вам информацию о последних трендах, лучшие предложения и советы по стилю."
                         "Не стесняйтесь задавать мне вопросы, и я всегда готов помочь вам с выбором. Давайте начнем, "
                         "что вас интересует сегодня?", reply_markup=buttons.start)


async def support(message: types.Message):
    await message.answer("Здесь будет контакты поддержки!")


async def back(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start)


async def about(message: types.Message):
    await message.answer('Что такое - OSOR ?! ⬇', reply_markup=buttons.start)


# ==================================================================================================================
async def all_products(message: types.Message):
    await message.answer('Вы зашли ко всем товарам! \n'
                         'Снизу выберите категорию! ⬇️', reply_markup=buttons.all_categories)


async def price_categories(message: types.Message):
    await message.answer("Выберите снизу ценовую категорию! ⬇️", reply_markup=buttons.price_categories)


async def order_products(message: types.Message):
    await message.answer("Вы зашли в заказы товара! \n"
                         "Снизу выберите категорию! ⬇️",
                         reply_markup=buttons.OrderWhereCategory)


async def try_on(message: types.Message):
    await message.answer('Вы зашли к примерке товара! \n'
                         'Снизу выберите категорию! ⬇️', reply_markup=buttons)


# ==================================================================================================================

def register_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(back, commands=['<назад'])
    dp.register_message_handler(about, commands=['О_нас!', 'about'])
    # ======================================================================
    dp.register_message_handler(all_products, commands=['Товары'])
    dp.register_message_handler(order_products, commands=['Заказать'])
    dp.register_message_handler(try_on, commands=['Примерить'])

    # ======================================================================
    dp.register_message_handler(price_categories, commands=['Все_товары!'])