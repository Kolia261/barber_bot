import asyncio
from aiogram import Bot, Dispatcher

from app.database.models import async_main
from app.user import router
from config import BOT_TOKEN


async def main():
    await async_main()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass