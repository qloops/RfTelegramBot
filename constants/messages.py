from enum import StrEnum


class BotMessages(StrEnum):
    PROFILE_NOT_FOUND = "Не удалось найти профиль."
    WELCOME = "Салам!"
    IM_BTN_SEND_PROFILE = "Отправить профиль в выбранный чат."
    NOT_YOUR_PROFILE = "Профиль не твой, я не стану его принимать!"
    PROFILE_EXPIRED = "Профиль устарел."
    REPLY_REQUIRED = "Используй ответ на сообщение, чтобы выполнить команду."
