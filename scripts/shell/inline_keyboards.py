from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# 1. Добавить сюда кнопку в клавиатуру
# 2. Добавить хэндлер для этой кнопки в handlers.py
# 3. Добавить состояния

def generating_filters_choice() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    budget_btn = InlineKeyboardButton(text='Бюджет', callback_data='budget_btn')
    snack_btn = InlineKeyboardButton(text='Наличие перекуса', callback_data='snack_btn')
    kkalories_btn = InlineKeyboardButton(text='Ккалории в день', callback_data='kkalories_btn')
    ready_btn = InlineKeyboardButton(text='Готово ✅', callback_data='ready_btn')
    kb.add(budget_btn, snack_btn, kkalories_btn, ready_btn)
    return kb


def snack_choice() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    snack_yes_btn = InlineKeyboardButton(text='Да', callback_data='snack_yes_btn')
    snack_no_btn = InlineKeyboardButton(text='Нет', callback_data='snack_no_btn')
    kb.add(snack_yes_btn, snack_no_btn)
    return kb


def confirm_filters() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    confirm_btn_edit = InlineKeyboardButton(text='Изменить', callback_data='confirm_btn_edit')
    confirm_btn_yes = InlineKeyboardButton(text='Подтвердить ✅', callback_data='confirm_btn_yes')
    kb.add(confirm_btn_edit, confirm_btn_yes)
    return kb
