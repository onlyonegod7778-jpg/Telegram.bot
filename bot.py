import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token ke sath quotes (" ") theek kar diye gaye hain
BOT_TOKEN = "8934221471:AAG828ldIoB5_mI1F0LDvnbDZUs-KgwTEXM"

bot = Bot(8934221471:AAG828ldIoB5_mI1F0LDvnbDZUs-KgwTEXM)
dp = Dispatcher()

# Jab user channel par join request bhejega
@dp.chat_join_request()
async def send_instructions_on_request(event: types.ChatJoinRequest):
    user_id = event.from_user.id
    user_name = event.from_user.first_name

    # 1. Message ka Caption / Instructions
    caption_text = (
        f"⚡ **WELCOME {user_name}!**\n\n"
        "🤖 **Channel Join karne ke steps:**\n\n"
        "💡 **How To Use:**\n"
        "1. Niche diye gaye link par register karein.\n"
        "2. Step complete karne ke baad admin verify karenge.\n\n"
        "👇 **Niche button par click karke shuru karein:**"
    )

    # 2. Buttons
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👉 Open Link", url="https://google.com"),
            ],
            [
                InlineKeyboardButton(text="💬 Help & Support", url="https://t.me/telegram"),
            ]
        ]
    )

    try:
        # Photo, caption aur buttons bhejna
        photo_url = "https://picsum.photos/800/400"
        await bot.send_photo(
            chat_id=user_id,
            photo=photo_url,
            caption=caption_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        print(f"Message sent to {user_name}")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    print("Bot chalu ho gaya...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
