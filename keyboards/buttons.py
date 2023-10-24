from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ======================================================================================================================
cancel_button = KeyboardButton('Отмена')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('да'),
                                          KeyboardButton('нет'))
# ======================================================================================================================
start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

review = KeyboardButton('/Написать_отзыв')

start.add(review)

finish_load_photos = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add \
    (KeyboardButton('/Это_все_сохранить_фото'))
