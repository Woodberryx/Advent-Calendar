from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6596148336:AAGkW5knNiqS5fKXZivjC4w51hYtzIFkiG4', parse_mode='HTML')
dp = Dispatcher(bot=bot)

#Keyboards
acm = InlineKeyboardMarkup()
acm.add(InlineKeyboardButton(text='Advent Calendar IT MY HUB', web_app=WebAppInfo(url='https://api.render.com/deploy/srv-cln3q8nfeb2c73egd0eg?key=L7aGrycYS9A')))

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('<b>Давайте начнем!🎄</b>\n'
                         'Чтобы начать, нажмите на кнопку ниже.',
                         reply_markup=acm)

if __name__ == '__main__':
    executor.start_polling(dp)