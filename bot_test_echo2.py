from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '7711974077:AAEmVh5klRDrrf1UD4Rl-eW55gCVKfDxagA'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer("Привет меня зовут Эхо бот! Напиши мне что нибудь")
    
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer("Напиши мне что нибудь и в ответ я тебе пришлю твоё же сообщение")

@dp.message()
async def send_echo(messege: Message):
    try:
        await messege.send_copy(chat_id=messege.chat.id)
    except:
        await messege.reply(
            text="Данный вид апдейта не поддерживается методом send_copy"
        )

if __name__ == '__main__':
    dp.run_polling(bot)