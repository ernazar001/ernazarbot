from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

from config import TOKEN
from chat import chatgpt_answer

import asyncio
import logging



logging.basicConfig(level=logging.INFO)



CHANNEL_ID = -1003219575359

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_hendler(message: types.Message):
    await message.answer("Salom nima qidirayapsiz")


@dp.message(F.text)
async def chat_hendler(message: types.Message):
    await bot.send_message(chat_id=CHANNEL_ID, text=message.text)
    javob = chatgpt_answer(message.text)
    await message.answer(javob)



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
