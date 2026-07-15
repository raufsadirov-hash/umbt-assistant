from aiogram.fsm.state import State, StatesGroup


class RegistrationForm(StatesGroup):
    fio = State()
    company = State()
    position = State()
    telegram = State()
    email = State()
