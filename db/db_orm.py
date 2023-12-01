import sqlite3
from aiogram import types, Dispatcher
from config import Admins, bot

from db import sql_queris


db = sqlite3.connect("db/review_db")
cursor = db.cursor()


async def sql_create():
    if db:
        print("База Бишкек подключена!")
    cursor.execute(sql_queris.CREATE_TABLE_REVIEW)
    db.commit()


async def sql_insert_review(state):
    async with state.proxy() as data:
        cursor.execute(sql_queris.INSERT_INTO_TABLE_REVIEW, tuple(data.values()))
        db.commit()


async def get_all_reviews(message: types.Message):
    reviews = cursor.execute(sql_queris.SELECT_CHECKS_REVIEWS).fetchall()

    for review in reviews:
        if message.from_user.id in Admins:
            await bot.send_photo(chat_id=message.from_user.id, photo=review["photo"],
                                 caption=f"Данные товара: \n"
                                         f"Артикуль товара: {review['articule']}"
                                         f"Название товара: {review['name']}\n"
                                         f"Отзыв о товаре: {review['review']}\n"
                                         f"Город: {review['city']}", )


def sql_get_ORM(dp: Dispatcher):
    dp.register_message_handler(get_all_reviews, commands=['все_отзывы!'])