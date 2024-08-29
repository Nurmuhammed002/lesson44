from aiogram import types
from aiogram.dispatcher import Dispatcher

async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для управления продуктами и заказами.")

async def info_command(message: types.Message):
    await message.answer("Этот бот помогает управлять продуктами и оформлять заказы. Для записи продукта используйте команду /add_product, для оформления заказа - /order.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(info_command, commands=["info"])
