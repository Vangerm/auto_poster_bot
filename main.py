import asyncio
import logging.config
from loger.logging_settings import logging_config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import load_config
from handlers import user_handlers, other_handlers, bot_hendlers


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info('Starting bot')

    # Получаем конфигурационные данные
    config = load_config()

    storage = MemoryStorage()

    # Заполняем конфигурационными данными переменные
    telegram_bot_token = config.tg_bot.token

    # Активация телеграмм бота
    bot: Bot = Bot(token=telegram_bot_token)
    dp: Dispatcher = Dispatcher(storage=storage)

    # bot_hendler в начало, обрабатываем состояния
    dp.include_router(bot_hendlers.router)
    dp.include_router(user_handlers.router)
    # other_handlers - должен быть последним
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
