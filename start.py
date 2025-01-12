from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import handlers.my_message as my_message

from bot_init import dp, bot
from states import Holat


@dp.message(Command("start"))
async def start_command(message: Message):
    await my_message.start_command(message)

@dp.message(Command("register"))
async def start_command(message: Message, state: FSMContext):
    await my_message.register_command(message,state=state)

@dp.message(Holat.name)
async def get_message(message: Message,state:FSMContext):
    await my_message.get_name(message=message, state=state)

@dp.message(Holat.username)
async def get_message(message: Message,state:FSMContext):
    await my_message.get_username(message=message,state=state)

@dp.message(Holat.check_data)
async def check_data(message: Message, state: FSMContext):
    await my_message.check_data(message=message,state=state)


async def main():
    await  dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())





