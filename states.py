
from aiogram.fsm.state import State, StatesGroup

class Holat(StatesGroup):
    name = State()
    username = State()
    check_data = State()