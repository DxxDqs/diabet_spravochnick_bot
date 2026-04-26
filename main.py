from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from handlers import user

async def main():
    load_dotenv()
    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass