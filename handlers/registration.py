from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from google_sheets import save_user
from states import RegistrationForm

router = Router()


@router.callback_query(F.data == "contest")
async def contest(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("👤 Введите ваше ФИО:")
    await state.set_state(RegistrationForm.fio)
    await callback.answer()


@router.message(RegistrationForm.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer("🏢 Введите название компании:")
    await state.set_state(RegistrationForm.company)


@router.message(RegistrationForm.company)
async def get_company(message: Message, state: FSMContext):
    await state.update_data(company=message.text)
    await message.answer("💼 Введите вашу должность:")
    await state.set_state(RegistrationForm.position)


@router.message(RegistrationForm.position)
async def get_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("📱 Введите ваш Telegram (@username или номер):")
    await state.set_state(RegistrationForm.telegram)


@router.message(RegistrationForm.telegram)
async def get_telegram(message: Message, state: FSMContext):
    await state.update_data(telegram=message.text)
    await message.answer("📧 Введите ваш E-mail:")
    await state.set_state(RegistrationForm.email)


@router.message(RegistrationForm.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)

    data = await state.get_data()

    save_user(data)

    await message.answer(
        f"""✅ Спасибо за участие!

Ваши данные:

👤 ФИО: {data['fio']}
🏢 Компания: {data['company']}
💼 Должность: {data['position']}
📱 Telegram: {data['telegram']}
📧 Email: {data['email']}

Ваша заявка успешно принята!"""
    )

    await state.clear()
