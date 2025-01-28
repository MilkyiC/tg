import os
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('token_bot')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('off')