
import requests as requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from constants import host

import constants

from data import config
from enum_constans import meeting_status_constant, waiting_status_constant, not_ready_status_constant
from states import Meeting_states
from enum_constans import change_profile, change_meeting_status
from keyboards.inline.callback_data import change_meeting_status_callback, edite_profile_callback
from keyboards.inline.inline_buttons import one_button, change_profile_or_status_button
from loader import dp
from request_to_server.requests import login


@dp.message_handler(Command("profile"))
async def profile(message: types.Message, state: FSMContext):
    # подбираем user_id
    user_id = message.from_user.id

    # определяем username бота
    url = "https://api.telegram.org/bot" + f'{config.BOT_TOKEN}' + "/getMe"
    payload = {}
    headers = {}
    bot_username = "@" + requests.request("POST", url, headers=headers, data=payload).json().get("result").get(
        "username")

    request_from_login = login(user_id, constants.a)
    # Если login вернул статус не 200(нет пользователя в базе), предлагаем пользователю зарегаться.
    # status = 200 - Все хорошо profile есть
    if request_from_login.status_code == 200:

        url = host + f'''/filling_profile/'''
        # text = f'''Привет 👋 {message.from_user.full_name}! На связи {bot_username}. Ты здесь не первый раз, не так ли?\nЯ о тебе кое-что помню: '''
        text = f'Это твой личный профиль'
        text += f'''\nСтатус поиска собеседника: '''
        meeting_status = request_from_login.json().get("meeting_status")
        if meeting_status == waiting_status_constant:
            text += f'''в поисках собеседника'''
        elif meeting_status == not_ready_status_constant:
            text += f'''не ищу собеседника'''
        elif meeting_status == meeting_status_constant:
            if request_from_login.json().get("companion") is not None:
                text += f'''общаюсь с @{request_from_login.json().get("companion")}'''
            else:
                text += f'''возникла ошибка при выводи статуса поиска встреч. Твой статус: "общаюсь ...", но партнер отсутсвует. Обратись с этой ошибкой в поддержку через /help'''
        else:
            text += f'''возникла ошибка со статусами поиска всреч. Обратись с этой ошибкой в поддержку через /help'''
        if request_from_login.json().get("skills") is not None:
            text += f'''\nТебя интересует: {request_from_login.json().get("skills")}'''
        text += f'''\nEmail📧: {request_from_login.json().get("email")}'''

        print(f'''***********skills:{request_from_login.json().get("skills")}''')
        text += "\nЧто-нибудь изменилось?"

        # Если статус пользователя "meetting", то отправляем сообщение пользователю только с одной кнопкой "изменить профиль".
        if meeting_status == meeting_status_constant:

            await message.answer(text, reply_markup=one_button(text_btn=change_profile,
                                callback_data=edite_profile_callback.new(status="edite_profile"),
                                url=requests.post(url, params={'token': request_from_login.json().get("token"),'contacts': user_id}).url))
        else:
            await message.answer(text, reply_markup=change_profile_or_status_button(change_profile,
                  requests.post(url, params={'token': request_from_login.json().get("token"),
                                             'contacts': user_id}).url, change_meeting_status))

    # profile не найден
    else:
        await message.answer(
            f"Привет 👋 {message.from_user.full_name}! На связи {bot_username}, я смотрю ты здесь первый раз. Нам "
            f"нужно пройти  регистрацию️", reply_markup=one_button(text_btn="регистрация",callback_data=change_meeting_status_callback.new(status="reg"), url=None))


