from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import main_menu, promotions_menu, back_button

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        """🏠 <b>UMBT Assistant</b>

Добро пожаловать!

Выберите интересующий раздел.""",
        parse_mode="HTML",
        reply_markup=main_menu()
    )


@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text(
        """🏠 <b>UMBT Assistant</b>

Добро пожаловать!

Выберите интересующий раздел.""",
        parse_mode="HTML",
        reply_markup=main_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "promotions")
async def promotions(callback: CallbackQuery):
    await callback.message.edit_text(
        """🎁 <b>Акции UMBT</b>

В этом разделе публикуются:

• Акции
• Конкурсы
• Специальные предложения""",
        parse_mode="HTML",
        reply_markup=promotions_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "academy")
async def academy(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎓 Раздел находится в разработке.",
        reply_markup=back_button()
    )
    await callback.answer()


@router.callback_query(F.data == "selection")
async def selection(callback: CallbackQuery):
    await callback.message.edit_text(
        "📐 Подбор оборудования скоро появится.",
        reply_markup=back_button()
    )
    await callback.answer()


@router.callback_query(F.data == "request")
async def request(callback: CallbackQuery):
    await callback.message.edit_text(
        "📞 Форма заявки скоро появится.",
        reply_markup=back_button()
    )
    await callback.answer()


@router.callback_query(F.data == "catalogs")
async def catalogs(callback: CallbackQuery):
    await callback.message.edit_text(
        "📚 Каталоги скоро будут доступны.",
        reply_markup=back_button()
    )
    await callback.answer()


@router.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    await callback.message.edit_text(
        """☎ Контакты

UMBT Midea Uzbekistan""",
        reply_markup=back_button()
    )
    await callback.answer()
