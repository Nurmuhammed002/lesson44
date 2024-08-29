from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from handlers import register_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



from aiogram import executor
from config import dp
from FSM_product import register_product_handlers
from FSM_order import register_order_handlers
from handlers import register_handlers
from db_main import create_db


def register_all_handlers():
    register_handlers(dp)
    register_product_handlers(dp)
    register_order_handlers(dp)

def setup_database():
    create_db()

if __name__ == "__main__":
    setup_database()
    register_all_handlers()
    executor.start_polling(dp, skip_updates=True)

