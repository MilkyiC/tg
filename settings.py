import json
import os
from dotenv import load_dotenv

load_dotenv()

file_stat = os.getenv('file_statistic')

def update_statistics(user_id,username):
    statistics = load_statistics()
    update_user_statistic(statistics, user_id, username)
    save_statistics(statistics)

def update_user_statistic(statistics,user_id,username):
    if str(user_id) not in statistics:
        statistics[str(user_id)] = {
            "username": username,
            "messages_count": 0
        }
    statistics[str(user_id)]["messages_count"] += 1

def load_statistics():
    try:
        with open(file_stat, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_statistics(statistics):
    with open(file_stat, 'w') as file:
        file.write(json.dumps(statistics, indent=2, ensure_ascii=False))

def echo_answer (message):
    if message.text == 'Привет':
        return 'Привет, Марат!'
    elif message.text == 'Помощь':
        return 'Ты писька!'
    else:
        return message.text