from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from config import STAFF
from aiogram import Bot
from config import TOKEN

bot = Bot(token=TOKEN)

class OrderFSM(StatesGroup):
    sku = State()
    size = State()
    quantity = State()
    contact = State()

async def start_order(message: types.Message):
    await OrderFSM.sku.set()
    await message.answer("Введите артикул товара")

async def add_order_sku(message: types.Message, state: FSMContext):
    await state.update_data(sku=message.text)
    await OrderFSM.next()
    await message.answer("Введите размер")


async def complete_order(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['contact'] = message.text
    await send_order_to_staff(data)
    await state.finish()
    await message.answer("Ваш заказ принят!")

async def send_order_to_staff(data):
    order_text = f"Новый заказ:\nАртикул: {data['sku']}\nРазмер: {data['size']}\nКоличество: {data['quantity']}\nКонтакт: {data['contact']}"
    for user_id in STAFF:
        await bot.send_message(user_id, order_text)

def register_order_handlers(dp: Dispatcher):
    dp.register_message_handler(start_order, commands="order", state="*")
    dp.register_message_handler(add_order_sku, state=OrderFSM.sku)
    dp.register_message_handler(complete_order, state=OrderFSM.contact)
