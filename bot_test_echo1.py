from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '7711974077:AAEmVh5klRDrrf1UD4Rl-eW55gCVKfDxagA'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer("Привет меня зовут Эхо бот! Напиши мне что нибудь")
    
    
async def process_help_command(message: Message):
    await message.answer("Напиши мне что нибудь и в ответ я тебе пришлю твоё же сообщение")


async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[-1].file_id)
    
async def send_echo(message: Message):
    await message.reply(text=message.text)
    

dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)