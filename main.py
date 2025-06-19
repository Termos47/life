from core.bot_initializer import bot, dp
from core.state_manager import AppState
from features.rss_parser import check_feeds
import asyncio

async def main():
    await dp.start_polling()
    while True:
        if AppState.is_running:
            await check_feeds()
        await asyncio.sleep(float(os.getenv('CHECK_INTERVAL', 300)))
