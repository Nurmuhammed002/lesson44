from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import ContentType
from db_main import save_product_to_db


class ProductFSM(StatesGroup):
    name = State()
    category = State()
    size = State()
    price = State()
    sku = State()
    photo = State()


async def start_add_product(message: types.Message):
    await ProductFSM.name.set()
    await message.answer("Введите название продукта")


async def add_product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await ProductFSM.next()
    await message.answer("Введите категорию продукта")




async def save_product_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.photo[-1].file_id
    data['photo'] = photo_id

    await save_product_to_db(data)
    await state.finish()
    await message.answer("Продукт успешно добавлен!")


def register_product_handlers(dp: Dispatcher):
    dp.register_message_handler(start_add_product, commands="add_product", state="*")
    dp.register_message_handler(add_product_name, state=ProductFSM.name)
    dp.register_message_handler(save_product_photo, content_types=ContentType.PHOTO, state=ProductFSM.photo)
