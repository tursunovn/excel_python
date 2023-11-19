from aiogram import Bot, Dispatcher, types, executor
from excel import *

from config import TOKEN_API
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

names = """
Xodimni yoki raqamni tanlang:
1 - ruslan
2 - izzat
3 - alisher"""

@dp.message_handler(commands=['start'])
async def take_name(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=names,
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['ruslan','1'])
async def ruslan(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Ruslanning qoldiq summasi -> " + str(rus),
                           parse_mode='HTML')

@dp.message_handler(commands=['izzat', '2'])
async def izzat(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Izzatning qoldiq summasi -> " + str(izza),
                           parse_mode='HTML')

@dp.message_handler(commands=['alisher', '3'])
async def alisher(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Alisherning qoldiq summasi -> " + str(alish),
                           parse_mode='HTML')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
