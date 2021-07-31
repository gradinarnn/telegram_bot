from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import registration_callback, edite_profile_callback, meeting_status_callback

regestration_button = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="регистрация",
                callback_data=registration_callback.new(status="reg")

            )
        ]
    ]
)


def change_profile_or_status_button(text_btn1, url):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_btn1,
                    callback_data=edite_profile_callback.new(status="edite_profile"),
                    url=url

                ),
                InlineKeyboardButton(
                    text="изменить статус поиска встречи",
                    callback_data=registration_callback.new(status="change_meeting_status")

                )
            ]
        ]
    )


def meeting_status_button(text_btn1, text_btn2):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [

                InlineKeyboardButton(
                    text=text_btn1,
                    callback_data=meeting_status_callback.new(status="meeting_status = waiting"),

                ),
                InlineKeyboardButton(
                    text=text_btn2,
                    callback_data=meeting_status_callback.new(status="meeting_status = not ready"),

                )
            ]
        ]
    )