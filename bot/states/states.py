from aiogram.fsm.state import State, StatesGroup


class NatsFillForm(StatesGroup):
    fill_id_vk_group = State()
    fill_id_tg_group = State()
