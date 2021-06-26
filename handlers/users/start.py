import sqlite3

import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import skills_categories_db

from keyboards.inline.callback_registration_or_profile_button import regestration_or_profile_button
from loader import dp, users_db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}!")

    count_users = users_db.count_users()[0]
    all_us = users_db.select_all_users()
    user = users_db.select_user(message.from_user.id)

    if user is not None:
        a = requests.post('http://127.0.0.1:8000/filling_profile/', params={'tg_prof': 'telega',
                                                                            'full_name': message.from_user.full_name,
                                                                            'email': 'сережа@mail.ru',
                                                                            'skills': 'какать, не мыться',
                                                                            'for_search': 'хочется общаться'
                                                                            })
        b = a.url
        await message.answer(
            f"Ты уже зарегестрирован. В базе таких как ты {count_users}: {all_us}. А еще ты лосось. ссылка {b}")

    else:

        await message.answer(text="Ты не зарегестрирован. Жми  на Кнопку ниже",
                             reply_markup=regestration_or_profile_button)
