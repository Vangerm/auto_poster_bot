import vk_api
import asyncio


class auto_poster:
    def __init__(self):
        pass


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