from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from settings import load_statistics,update_statistics,echo_answer

router=Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Можёшь написать Привет, Помощь, /stat')

@router.message(Command('stat'))
async def cmd_stat(message: Message):
    user_id = message.from_user.id
    statistics = load_statistics()
    await message.answer(str(statistics[str(user_id)]["messages_count"]))

@router.message()
async def echo_message(message: types.Message):
    await message.answer(echo_answer(message))
    user_id = message.from_user.id
    username = message.from_user.username or 'Неизвестный'
    update_statistics(user_id,username)




