import json
from typing import Any

from app.models import MessageModel
from settings import FILE_STATISTICS_NAME


def update_statistics(message_info: MessageModel) -> None:
    """
    Обновляет статистику пользователя, загружая текущие данные, обновляя их и сохраняя обратно.

    Аргументы:
        user_id (str): Идентификатор пользователя, чью статистику необходимо обновить.
        username (str): Имя пользователя.
    """
    statistics = load_statistics()
    update_user_statistic(statistics, message_info.user_id, message_info.username)
    save_statistics(statistics)


def update_user_statistic(statistics: dict[str, Any], user_id: int, username: str) -> None:
    """
    Обновляет статистику пользователя, добавляя или обновляя информацию о количестве сообщений.

    Аргументы:
        statistics (dict): Словарь, содержащий статистику пользователей, где ключом является
                           идентификатор пользователя (user_id), а значением - информация о пользователе.
        user_id (str): Идентификатор пользователя, чью статистику необходимо обновить.
        username (str): Имя пользователя, которое будет добавлено, если пользователь новый.

    """
    if str(user_id) not in statistics:
        statistics[str(user_id)] = {"username": username, "messages_count": 0}
    statistics[str(user_id)]["messages_count"] += 1


def load_statistics() -> dict[str, Any]:
    """
    Загружает статистику из файла в формате JSON.

    Возвращает:
        dict: Словарь, содержащий загруженные статистические данные.
              Если файл не найден или данные некорректны, возвращается пустой словарь.
    """
    try:
        with open(FILE_STATISTICS_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_statistics(statistics: dict[str, Any]) -> None:
    """
    Функция записывает в файл file_stat переменную statistics

    Аргументы:
        statistics (dict): Словарь, содержащий статистические данные,
                           которые необходимо сохранить.
    """
    with open(FILE_STATISTICS_NAME, "w") as file:
        file.write(json.dumps(statistics, indent=2, ensure_ascii=False))


def get_answer(message: MessageModel) -> str:
    """
    Функция возвращает ответ на сообщение пользователя в зависимости от его текста.

    Аргументы:
        message(MessageModel): Объект сообщения, содержащий текст, который нужно обработать.

    Возвращает:
        Ответ на сообщение в строковом типе
    """
    if not isinstance(message.text, str):
        return "Извините, я еще не умею обрабатывать такие сообщения "
    match message.text:
        case "Привет":
            return "Привет!"
        case "Помощь":
            return "Вы можете узнать статистику при помощи команды /stat"
        case "Как дела?":
            return "Хорошо, а ваши?"
        case _:
            return message.text
