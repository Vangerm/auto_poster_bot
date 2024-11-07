import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup


logger = logging.getLogger(__name__)

router = Router()

# Создаем "базу данных" пользователей
user_dict: dict = {}


class FSMFillForm(StatesGroup):
    fill_id_vk_group = State()
    fill_id_tg_group = State()


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из настройки автопоста.\n\n'
             'Чтобы снова перейти к настройке втопоста - '
             'отправьте команду /autopost.'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message, state: FSMContext):
    await message.answer(
        text='Отменять нечего. Вы не настраиваете автопост.\n\n'
        'Чтобы перейти к настройке автопоста - '
        'отправьте команду /autopost.'
        )


@router.message(Command(commands='autopost'), StateFilter(default_state))
async def process_autopost_command(message: Message, state: FSMContext):
    logger.info(f'{message.chat.username} ({message.chat.id}) '
                '- start fill autopost')
    await message.answer(text='Пожалуйста, введите id группы vk.')
    await state.set_state(FSMFillForm.fill_id_vk_group)


@router.message(StateFilter(FSMFillForm.fill_id_vk_group),
                lambda x: x.text.isdigit())
async def process_autopost_id_vk_group(message: Message, state: FSMContext):
    await state.update_data(id_vk_group=int(message.text))
    await message.answer(
        text='Спасибо!\n\nА теперь введите id группы tg.'
    )
    await state.set_state(FSMFillForm.fill_id_tg_group)


@router.message(StateFilter(FSMFillForm.fill_id_vk_group))
async def warning_not_id_vk_group(message: Message):
    await message.answer(
        text='id группы vk должен быть числом.'
    )


@router.message(StateFilter(FSMFillForm.fill_id_tg_group),
                lambda x: x.text.isdigit())
async def process_autopost_id_tg_group(message: Message, state: FSMContext):
    await state.update_data(id_tg_group=int(message.text))

    user_dict[message.from_user.id] = await state.get_data()

    await state.clear()
    print(user_dict)

    await message.answer(
        text='Ваш бот запущен, наслаждайтесь!'
    )


@router.message(StateFilter(FSMFillForm.fill_id_tg_group))
async def warning_not_id_tg_group(message: Message):
    await message.answer(
        text='id группы tg должен быть числом.'
    )


@router.message(Command(commands='showautopost'), StateFilter(default_state))
async def process_showautopost_command(message: Message):
    if message.from_user.id in user_dict:
        await message.answer(
            text=f'id vk - {user_dict[message.from_user.id]['id_vk_group']}'
            f'\nid tg - {user_dict[message.from_user.id]['id_tg_group']}'
        )
    else:
        await message.answer(
            text='Вы еще не настраивали бота,'
            'для настройки напишите мне /autopost'
        )
