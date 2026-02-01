from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '7711974077:AAEmVh5klRDrrf1UD4Rl-eW55gCVKfDxagA'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer("Привет меня зовут Эхо бот , напиши что нибудь")
    
    
@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer("Напиши мне что нибудь и в ответ я тебе пришлю твоё сообщение")

@dp.message(F.text)
async def send_echo(message: Message):
    await message.reply(message.text)

@dp.message(F.photo)
async def on_photo(message: Message):
    caption = message.caption or "(без надписи)"
    await message.reply(f"Вижу фото Подпись: {caption}")
    

if __name__ == '__main__':
    dp.run_polling(bot)
    