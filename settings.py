import json
import os
from dotenv import load_dotenv

load_dotenv()

file_stat = os.getenv('file_statistic')

def update_statistics(user_id,username):
    """
    Обновляет статистику пользователя, загружая текущие данные, обновляя их и сохраняя обратно.

    Аргументы:
        user_id (str): Идентификатор пользователя, чью статистику необходимо обновить.
        username (str): Имя пользователя, которое будет добавлено, если пользователь новый.
    """
    statistics = load_statistics()
    update_user_statistic(statistics, user_id, username)
    save_statistics(statistics)

def update_user_statistic(statistics,user_id,username):
    """
    Обновляет статистику пользователя, добавляя или обновляя информацию о количестве сообщений.

    Аргументы:
        statistics (dict): Словарь, содержащий статистику пользователей, где ключом является
                           идентификатор пользователя (user_id), а значением - информация о пользователе.
        user_id (str): Идентификатор пользователя, чью статистику необходимо обновить.
        username (str): Имя пользователя, которое будет добавлено, если пользователь новый.

    """
    if str(user_id) not in statistics:
        statistics[str(user_id)] = {
            "username": username,
            "messages_count": 0
        }
    statistics[str(user_id)]["messages_count"] += 1

def load_statistics():
    """
    Загружает статистику из файла в формате JSON.

    Аргументы:
        file_stat (str): Путь к файлу, из которого будет загружена статистика.
                         Если файл не существует или содержит некорректные данные,
                         будет возвращен пустой словарь.

    Возвращает:
        dict: Словарь, содержащий загруженные статистические данные.
              Если файл не найден или данные некорректны, возвращается пустой словарь.
    """
    try:
        with open(file_stat, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_statistics(statistics):
    """
    Функция записывает в файл file_stat переменную statistics

    Аргументы:
        statistics (dict): Словарь, содержащий статистические данные,
                           которые необходимо сохранить.
        file_stat (str): Путь к файлу, в который будет сохранена статистика.
                         Если файл не существует, он будет создан.
    """
    with open(file_stat, 'w') as file:
        file.write(json.dumps(statistics, indent=2, ensure_ascii=False))

def echo_answer (message):
    """
    Функция возвращает ответ на сообщение пользователя в зависимости от его текста.

    Аргументы:
        message: Объект сообщения, содержащий текст, который нужно обработать.
                 Объект должен иметь строковый тип.

    Возвращает:
        Ответ на сообщение в строковом типе
        """
    if message.text == 'Привет':
        return 'Привет, Марат!'
    elif message.text == 'Помощь':
        return 'Ты писька!'
    else:
        return message.text