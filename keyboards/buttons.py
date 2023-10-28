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
back = KeyboardButton('/<назад')
# ======================================================================================================================
yesno = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2).add(KeyboardButton('Да'),
                     KeyboardButton('Нет'),
                     cancel_button)

# ======================================================================================================================
start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

all_products = KeyboardButton('/Товары')
review = KeyboardButton('/Написать_отзыв')
order = KeyboardButton('/Заказать')
try_on = KeyboardButton('/Примерить')
about = KeyboardButton('/О_нас!')

start.add(all_products, order, try_on, review, about)

# ======================================================================================================================

OrderWhereCategory = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2).add(KeyboardButton('/Обувь'),
                     KeyboardButton('/Нижнее_белье'),
                     KeyboardButton('/Акссесуары'),
                     KeyboardButton('/Верхняя_одежда'),
                     KeyboardButton('/Штаны'),
                     back)

city_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2
                                  ).add(KeyboardButton('Бишкек'),
                                        KeyboardButton('ОШ'),
                                        KeyboardButton('Москва 1-филиал'),
                                        KeyboardButton('Москва 1-филиал'))

# ======================================================================================================================

all_categories = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2).add(KeyboardButton('/Обувь'),
                     KeyboardButton('/Нижнее_белье'),
                     KeyboardButton('/Акссесуары'),
                     KeyboardButton('/Верхняя_одежда'),
                     KeyboardButton('/Штаны'),
                     KeyboardButton('/Все_товары!'),
                     back)

price_categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True,
                                       row_width=2
                                       ).add(KeyboardButton('До_2000сом'),
                                             KeyboardButton('2000_4000сом'),
                                             KeyboardButton('4000_6000сом'),
                                             KeyboardButton('+6000сом'),
                                             KeyboardButton("Все_цены!"))
# ======================================================================================================================
