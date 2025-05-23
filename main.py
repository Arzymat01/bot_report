import asyncio
from aiogram import Bot, Dispatcher
from handlers.handlers import dp
from config import API_TOKEN

async def main():
    print("Бот запущен...")
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())