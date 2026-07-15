import asyncio
import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import BOT_TOKEN
from google_sheets import save_user


# ----- НУЖНО ДЛЯ RENDER -----
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


Thread(target=run_server, daemon=True).start()
# ----------------------------


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class Form(StatesGroup):
    fio = State()
    company = State()
    position = State()
    telegram = State()
    email = State()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text="🎁 Принять участие",
        callback_data="contest"
    )

    await message.answer(
        """⚽ <b>Midea × ФК «Барселона» — партнерство чемпионов!</b>

Компания <b>Midea</b> стала официальным партнером ФК «Барселона».

🎉 В честь этого события UMBT запускает розыгрыш!

🏆 <b>Главный приз:</b>
Приглашение на двоих на просмотр финала Чемпионата мира 2026 в ресторане Brasserie.

Нажмите кнопку ниже, чтобы принять участие.""",
        parse_mode="HTML",
        reply_markup=kb.as_markup()
    )


@dp.callback_query(F.data == "contest")
async def contest(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("👤 Введите ваше ФИО:")
    await state.set_state(Form.fio)
    await callback.answer()


@dp.message(Form.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer("🏢 Введите название компании:")
    await state.set_state(Form.company)


@dp.message(Form.company)
async def get_company(message: Message, state: FSMContext):
    await state.update_data(company=message.text)
    await message.answer("💼 Введите вашу должность:")
    await state.set_state(Form.position)


@dp.message(Form.position)
async def get_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("📱 Введите ваш Telegram (@username или номер):")
    await state.set_state(Form.telegram)


@dp.message(Form.telegram)
async def get_telegram(message: Message, state: FSMContext):
    await state.update_data(telegram=message.text)
    await message.answer("📧 Введите ваш E-mail:")
    await state.set_state(Form.email)


@dp.message(Form.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)

    data = await state.get_data()
    save_user(data)

    text = f"""
✅ Спасибо за участие!

Ваши данные:

👤 ФИО: {data['fio']}
🏢 Компания: {data['company']}
💼 Должность: {data['position']}
📱 Telegram: {data['telegram']}
📧 Email: {data['email']}

Ваша заявка успешно принята!
"""

    await message.answer(text)

    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
