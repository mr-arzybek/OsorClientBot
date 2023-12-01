from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import buttons
from datetime import datetime


# =======================================================================================================================


class regist_fsm(StatesGroup):
    name = State()
    instagram = State()
    phone = State()
    submit = State()


async def fsm_start(message: types.Message):
    await regist_fsm.name.set()
    await message.answer("Как вас зовут?", reply_markup=buttons.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await regist_fsm.next()
    await message.answer("Ваш инстаграм!?")


async def load_inst(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["inst"] = message.text
    await regist_fsm.next()
    await message.answer("Ваш номер телефона!?\n")


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date"] = datetime.now()
        await message.answer(f"Ваше имя: {data['articule']}"
                             f"Ваш инстаграм: {data['name']}\n"
                             f"Ваш номер телефона: {data['review']}\n")
    await regist_fsm.submit.set()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "да":
            if data['city'] == 'Бишкек':
                # Запись в базу данных!
                pass

            elif data['city'] == 'ОШ':
                # Запись в базу данных!
                pass

            elif data['city'] == 'Москва 1-филиал':
                # Запись в базу данных!
                pass

            elif data['city'] == 'Москва 2-филиал':
                # Запись в базу данных!
                pass

            await message.answer('Готово!', reply_markup=buttons.start)
            await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.start)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)


# =======================================================================================================================


def register_review(dp: Dispatcher):
    dp.register_message_handler(
        cancel_reg, Text(equals="Отмена", ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=["Регистрация!"])

    dp.register_message_handler(load_name, state=regist_fsm.name)
    dp.register_message_handler(load_inst, state=regist_fsm.instagram)
    dp.register_message_handler(load_phone, state=regist_fsm.phone)

    dp.register_message_handler(load_submit, state=regist_fsm.submit)
