from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def send_empty_message(message: Message):
    if message.forward_origin and\
       message.forward_origin.type == 'channel':
        chat_id = message.forward_origin.chat.id
        await message.answer(f'id чата/группы: {chat_id}')
    else:
        if message.forward_origin and\
           message.forward_origin.type == 'user':
            chat_id = message.forward_origin.sender_user.id
        else:
            chat_id = message.chat.id
        await message.answer(f'id пользователя: {chat_id}')
