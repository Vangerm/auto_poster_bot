import logging
from aiogram import Router
from config_data.config import load_config
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


logger = logging.getLogger(__name__)

router = Router()
config = load_config()
admin_ids = config.tg_bot.admin_ids


@router.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'{message.chat.username} ({message.chat.id}) - start bot')
    await message.answer(
        text='Добрый день, меня зовут VK_POSTER!\n\n'
        'Я помогу вам дублировать новости '
        'из вашей группы вк в телеграмм группу.\n\n'
        'Напишите мне /autopost '
        'для начала настройки автопоста.\n\n'
        'Триал версия состовляет 1 месяц, '
        'для просмотра тарифов напишите /info.\n\n'
        'Перед началом работы узнайте id группы вк '
        '(убедитесь что она открыта), '
        'а так же id группы тг.\n'
        'Можете переслать сообщание из группы тг мне, а'
        'я подскажу (копировать id группы нужно без минуса!).'
        )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Напишите мне /autopost '
        'для начала настройки автопоста.\n\n'
        'Триал версия состовляет 1 месяц, '
        'для просмотра тарифов напишите /tariffs.\n\n'
        'Перед началом работы узнайте id группы вк '
        '(убедитесь что она открыта), '
        'а так же id группы тг.\n'
        'Можете переслать сообщание из группы тг мне, а'
        'я подскажу (копировать id группы нужно без минуса!).'
        '\n\nВ дальнейшем наш бот будет развиваться, '
        'будем рады обратной связи.\n\n'
        'Напишите мне /feedback и оставте обратную связь.'
        )


@router.message(Command(commands='tariffs'))
async def process_tariffs_command(message: Message):
    await message.answer(
        text='Мы пока работаем над этим, ожидайте.'
        )


@router.message(Command(commands='feedback'))
async def process_feedback_command(message: Message):
    await message.answer(
        text='Мы пока работаем над этим, ожидайте.'
        )


@router.message(Command(commands='support'))
async def process_support_command(message: Message):
    await message.answer(
        text='Мы пока работаем над этим, ожидайте.'
        )


@router.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    await message.answer(
        text='Отменять нечего. Вы не настраиваете автопост.\n\n'
        'Чтобы перейти к настройке автопоста - '
        'отправьте команду /autopost.'
        )
