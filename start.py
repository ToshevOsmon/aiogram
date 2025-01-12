from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot_init import dp, bot
from states import Holat



@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Bot has been started")
     # await message.answer("Test message")
     # await bot.send_message(chat_id=message.from_user.id, text="Test")

@dp.message(Command("register"))
async def start_command(message: Message, state: FSMContext):
    await message.reply("Inter your name:")
    await state.set_state(Holat.name)

@dp.message(Holat.name)
async def get_message(message: Message,state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Enter your username")
    await state.set_state(Holat.username)

@dp.message(Holat.username)
async def get_message(message: Message,state:FSMContext):
    uname = message.text
    await state.update_data(username=uname)
    data = await state.get_data()
    await message.answer(f"I have got your data. Is it corrent?\n\nName:{data["name"]}\nUsername: {data["username"]}\n\nSend \"Yes\" to confirm or \"No\" to edit")
    await state.set_state(Holat.check_data)

@dp.message(Holat.check_data)
async def check_data(message: Message, state: FSMContext):
    text = message.text
    if text.lower() == "yes":
        data = await state.get_data()
        #  print(data)
        await message.answer("Your data has been saved")
        await state.clear()
    elif text.lower() == "no":
        await message.answer("Enter your name:")
        await state.set_state(Holat.name)
    else:
        await message.answer("You need to send \"Yes\" or \"No\"")

async def main():
    await  dp.start_polling(bot)


if __name__=="__main__":
    import asyncio
    asyncio.run(main())





