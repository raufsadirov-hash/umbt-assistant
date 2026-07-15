import asyncio
import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.registration import router as registration_router


# ---------- Render ----------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


Thread(target=run_server, daemon=True).start()
# ----------------------------


bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(registration_router)


async def main():
    me = await bot.get_me()

    print(f"Бот @{me.username} запущен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
