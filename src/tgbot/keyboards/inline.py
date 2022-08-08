from aiogram import types


def start_keyboard() -> types.InlineKeyboardMarkup:
    """
    This function create start keyboard with 4 buttons
    """

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            'Богослужение', callback_data='worship'
        ),
        types.InlineKeyboardButton(
            'Новости', callback_data='news'
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            'Контакты', callback_data='contacts'
        ),
        types.InlineKeyboardButton(
            'Хочу служить', callback_data='service'
        )
    )

    return keyboard
