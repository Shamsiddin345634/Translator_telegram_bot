import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from config import API_TOKEN
from buttons import *
from database import Translate
from googletrans import Translator
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = Translate()
translate = Translator()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    db.create_table()
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    username = message.from_user.username
    
    x = db.user_exist(user_id)
    if x is None:
        db.add_user(user_id, firstname, username)
        await bot.send_message(1813994648, f"User ID: {user_id}\nName: {firstname}\nUsername: @{username}")
        await message.answer(f"Здравствуйте @{message.chat.username}!\nДобро пожаловать на @perevodcheek_bot")
        await message.answer("Введите текст:" )
    else:
        await message.answer(f"С возвращением @{message.chat.username}!\nДобро пожаловать на @perevodcheek_bot")
        await message.answer("Введите текст:" )
    
        
@dp.message_handler(commands=['alluser'], user_id=1813994648)
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("tarjima.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(user_id) FROM users")
    allusers = cursor.fetchall()

    for i in allusers:
        await message.reply(f"Foydalanuvchilar soni: {i[0]} ta")
@dp.message_handler()
async def echo(message: types.Message):
    global word
    word = message.text
    await message.answer("Какой язык вы хотите перевести:", reply_markup = til)
    
@dp.callback_query_handler(text = "ru")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "ru")
    await call.message.answer(result.text)
    
@dp.callback_query_handler(text = "uz")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "uz")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "ar")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "ar")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "es")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "es")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "zh-cn")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "zh-cn")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "de")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "de")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "en")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "en")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "fr")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "fr")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "tr")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "tr")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "ja")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "ja")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "kr")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "ko")
    await call.message.answer(result.text)
@dp.callback_query_handler(text = "kz")
async def echo(call: CallbackQuery):
    result = translate.translate(word, dest = "kk")
    await call.message.answer(result.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)