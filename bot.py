import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Aapka naya Token
BOT_TOKEN = "8934221471:AAHXHDEtT-3td1pRy5lH2c9waujZyh5TPzQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Jab user channel par join request bhejega
@dp.chat_join_request()
async def send_instructions_on_request(event: types.ChatJoinRequest):
    user_id = event.from_user.id
    user_name = event.from_user.first_name

    caption_text = (
        f"⚡ **WELCOME {user_name}!**\n\n"
        "🤖 **Channel Join karne ke steps:**\n\n"
        "💡 **How To Use:**\n"
        "1. Niche diye gaye link par register karein.\n"
        "2. Step complete hone ke baad admin verify karenge.\n\n"
        "👇 **Niche button par click karke shuru karein:**"
    )

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
        photo_url = "https://picsum.photos/800/400"
        await bot.send_photo(
            chat_id=user_id,
            photo=photo_url,
            caption=caption_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        print(f"Instruction sent to {user_name}")
    except Exception as e:
        print(f"Error: {e}")

# Render server crash na ho iske liye dummy web handler
async def handle_ping(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print("Bot chalu ho gaya...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
