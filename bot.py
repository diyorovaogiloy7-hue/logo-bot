import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7972361877:AAGFlyNmOp_0FBUCrvKhklafDWD979iCRwg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    text = (
        "🎨 Assalomu alaykum!\n\n"
        "Men Logo Design botman.\n"
        "Logo buyurtma berish uchun ma'lumot yuboring:\n\n"
        "1️⃣ Kompaniya nomi\n"
        "2️⃣ Ranglar\n"
        "3️⃣ Qanday uslub\n"
        "4️⃣ Aloqa raqamingiz"
    )
    await message.answer(text)

@dp.message()
async def get_order(message: Message):
    await message.answer(
        "✅ Buyurtmangiz qabul qilindi!\n"
        "Tez orada siz bilan bog'lanamiz."
    )

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())