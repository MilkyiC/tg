from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from .models import MessageModel
from .services import get_answer, load_statistics, update_statistics

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Обрабатывает команду запуска и отправляет приветственное сообщение пользователю.

    Аргументы:
        message (Message): Объект сообщения, содержащий информацию о команде и отправителе.
    """
    await message.reply("Можёшь написать Привет, Помощь, /stat")


@router.message(Command("stat"))
async def cmd_stat(message: Message):
    """
    Обрабатывает команду статистики и отправляет пользователю количество сообщений,
    отправленных им в чат.

    Аргументы:
        message (Message): Объект сообщения, содержащий информацию о команде и отправителе.
    """
    user_id = message.from_user.id
    statistics = load_statistics()
    if str(user_id) not in statistics:
        await message.answer('Вы ещё не отправляли сообщений.')
    else:
        await message.answer(str(statistics[str(user_id)]["messages_count"]))


@router.message()
async def echo_message(message: types.Message):
    """
    Обрабатывает входящее сообщение, отправляет его обратно пользователю и обновляет статистику.

    Аргументы:
        message (types.Message): Объект сообщения, содержащий информацию о пользователе и тексте сообщения.
    """
    message_info = MessageModel(user_id=message.from_user.id, username=message.from_user.username, text=message.text)
    await message.answer(get_answer(message_info))
    update_statistics(message_info)
