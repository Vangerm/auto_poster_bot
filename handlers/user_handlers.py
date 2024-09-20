import vk_api
import asyncio
import logging
from aiogram import Router, F
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
    await message.answer(text='Добрый день, меня зовут VK_POSTER!\n\n'
                         'Я помогу вам дублировать новости '
                         'из вашей группы вк в телеграмм группу.\n\n'
                         'Напишите мне /startpost '
                         'для начала настройки автопоста.\n\n'
                         'Триал версия состовляет 1 месяц, '
                         'для просмотра тарифов напишите /info\n\n'
                         'Перед началом работы узнайте id группы вк '
                         '(убедитесь что она открыта), '
                         'а так же id группы тг.\n'
                         'Можете переслать сообщание из группы тг сюда.')


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='Напишите мне /startpost '
                         'для начала настройки автопоста.\n\n'
                         'Триал версия состовляет 1 месяц, '
                         'для просмотра тарифов напишите /info\n\n'
                         'Перед началом работы узнайте id группы вк '
                         '(убедитесь что она открыта), '
                         'а так же id группы тг.\n'
                         'Можете переслать сообщание из группы тг сюда.\n\n'
                         'В дальнейшем наш бот будет развиваться, '
                         'будем рады обратной связи.\n\n'
                         'Напишите мне /feedback и оставте обратную связь.')


# @router.message(Command(commands='startbot') and F.from_user.id.in_(admin_ids))
# async def process_start_bot_command(message: Message):
#     logger.info('Start check vk news')
#     telegram_group_id = config.tg_bot.group_id
#     vk_bot_token = config.vk_bot.token
#     vk_group_id = config.vk_bot.group_id

#     post_id = 0

#     # подключение по токену
#     vk_session = vk_api.VkApi(token=vk_bot_token)
#     # подключение к вк
#     vk = vk_session.get_api()

#     while True:
#         vk_post_info = vk.wall.get(owner_id=vk_group_id, count=2)
#         is_pinned = 0

#         if vk_post_info['items'][0].get('is_pinned', 0):
#             is_pinned = 1

#         vk_post = vk_post_info['items'][is_pinned]

#         if vk_post['id'] != post_id:
#             post_id = vk_post['id']
#             attachments = vk_post['attachments']

#             if len(attachments):
#                 if attachments[0]['type'] == 'photo':
#                     url = attachments[0]['photo']['orig_photo']['url']
#                 photo = URLInputFile(url)
#                 await message.bot.send_photo(
#                         telegram_group_id,
#                         photo,
#                         caption=vk_post['text']
#                     )
#             else:
#                 await message.bot.send_message(
#                         telegram_group_id,
#                         vk_post['text']
#                     )
#         await asyncio.sleep(1800)
