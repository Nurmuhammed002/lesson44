from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class ProductFSM(StatesGroup):
    name = State()
    category = State()
    size = State()
    price = State()
    sku = State()
    photo = State()


