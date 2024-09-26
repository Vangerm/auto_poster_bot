import asyncio
import logging.config
from loger.logging_settings import logging_config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config_data.config import load_config
from handlers import (user_handlers,
                      other_handlers,
                      bot_hendlers,
                      admin_handlers)


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info('Starting bot')

    # Получаем конфигурационные данные
    config = load_config()

    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)

    # Заполняем конфигурационными данными переменные
    telegram_bot_token = config.tg_bot.token

    # Активация телеграмм бота
    bot: Bot = Bot(token=telegram_bot_token)
    dp: Dispatcher = Dispatcher(storage=storage)

    dp['admin_ids'] = config.tg_bot.admin_ids

    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(bot_hendlers.router)

    # other_handlers - должен быть последним
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
