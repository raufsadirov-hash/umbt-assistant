from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from google_sheets import save_user
from states import RegistrationForm

router = Router()


# ==========================================
# Открытие страницы мероприятия
# ==========================================
@router.callback_query(F.data == "contest")
async def contest(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🎁 Принять участие",
        callback_data="register:barcelona"
    )

    kb.button(
        text="⬅️ Назад",
        callback_data="promotions"
    )

    kb.adjust(1)

    await callback.message.edit_text(
        """⚽ <b>Midea × ФК «Барселона» — партнерство чемпионов!</b>

Компания <b>Midea</b> стала официальным партнером футбольного клуба «Барселона».

🎉 В честь этого события UMBT запускает розыгрыш.

🏆 <b>Главный приз:</b>

Приглашение на двоих на просмотр финала Чемпионата мира 2026 в ресторане Brasserie.

Нажмите <b>«Принять участие»</b>, чтобы зарегистрироваться.""",
        parse_mode="HTML",
        reply_markup=kb.as_markup()
    )

    await callback.answer()


# ==========================================
# Начало регистрации
# ==========================================
@router.callback_query(F.data.startswith("register:"))
async def start_registration(callback: CallbackQuery, state: FSMContext):

    event_id = callback.data.split(":")[1]

    await state.update_data(event=event_id)

    await callback.message.answer(
        "👤 Введите ваше ФИО:"
    )

    await state.set_state(RegistrationForm.fio)

    await callback.answer()


# ==========================================
# ФИО
# ==========================================
@router.message(RegistrationForm.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)

    await message.answer(
        "🏢 Введите название компании:"
    )

    await state.set_state(RegistrationForm.company)


# ==========================================
# Компания
# ==========================================
@router.message(RegistrationForm.company)
async def get_company(message: Message, state: FSMContext):
    await state.update_data(company=message.text)

    await message.answer(
        "💼 Введите вашу должность:"
    )

    await state.set_state(RegistrationForm.position)


# ==========================================
# Должность
# ==========================================
@router.message(RegistrationForm.position)
async def get_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)

    await message.answer(
        "📱 Введите ваш Telegram (@username или номер):"
    )

    await state.set_state(RegistrationForm.telegram)


# ==========================================
# Telegram
# ==========================================
@router.message(RegistrationForm.telegram)
async def get_telegram(message: Message, state: FSMContext):
    await state.update_data(telegram=message.text)

    await message.answer(
        "📧 Введите ваш E-mail:"
    )

    await state.set_state(RegistrationForm.email)


# ==========================================
# Email
# ==========================================
@router.message(RegistrationForm.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)

    data = await state.get_data()

    save_user(data)

    await message.answer(
        f"""✅ Спасибо за регистрацию!

📌 Мероприятие: {data['event']}

👤 ФИО: {data['fio']}
🏢 Компания: {data['company']}
💼 Должность: {data['position']}
📱 Telegram: {data['telegram']}
📧 Email: {data['email']}

Ваша заявка успешно принята!"""
    )

    await state.clear()
