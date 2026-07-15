from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 Акции",
                    callback_data="promotions"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎓 Академия UMBT",
                    callback_data="academy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📐 Подбор оборудования",
                    callback_data="selection"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📞 Оставить заявку",
                    callback_data="request"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📚 Каталоги",
                    callback_data="catalogs"
                )
            ],
            [
                InlineKeyboardButton(
                    text="☎ Контакты",
                    callback_data="contacts"
                )
            ]
        ]
    )


def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_main"
                )
            ]
        ]
    )


def promotions_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚽ Конкурс Midea × Barcelona",
                    callback_data="contest"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_main"
                )
            ]
        ]
    )
