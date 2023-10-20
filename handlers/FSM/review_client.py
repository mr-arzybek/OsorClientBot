# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from keyboards import buttons

from datetime import datetime


# =======================================================================================================================

class review_fsm(StatesGroup):
    name = State()  # Название товара
    review = State()
    city = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    await review_fsm.name.set()
    await message.answer('Название товара?', reply_markup=buttons.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await review_fsm.next()
    await message.answer('Отзыв о товаре!?\n'
                         '?/5')


async def load_review(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['review'] = message.text
    await review_fsm.next()
    await message.answer('Филиал!?')


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await review_fsm.next()
    await message.answer('Фото товара?')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные товара: \n"
                    f"Название товара: {data['name']}\n"
                    f"Отзыв о товаре: {data['review']}\n"
                    f"Город: {data['city']}")
    await review_fsm.next()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                # Запись в базу данных!
                await message.answer('Готово!', reply_markup=buttons.)
                await state.finish()

            elif data['city'] == 'ОШ':
                # Запись в базу данных!
                await message.answer('Готово!', reply_markup=buttons.)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                # Запись в базу данных!
                await message.answer('Готово!', reply_markup=buttons.)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                # Запись в базу данных!
                await message.answer('Готово!', reply_markup=buttons.)
                await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.)


# =======================================================================================================================

def register_review(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['Написать_отзыв'])

    dp.register_message_handler(load_name, state=review_fsm.name)
    dp.register_message_handler(load_review, state=review_fsm.review)
    dp.register_message_handler(load_city, state=review_fsm.city)
    dp.register_message_handler(load_photo, state=review_fsm.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=review_fsm.submit)
