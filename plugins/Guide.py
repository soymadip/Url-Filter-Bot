

import re
import pyrogram
import asyncio

from pyrogram import (
    filters,
    Client
)

from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot import Bot
from script import script
from config import MAINCHANNEL_ID, ADMINS, SHIFT_CHANNEL



@Client.on_message(filters.incoming & filters.text )
async def filter(client: Bot, message: Message):
    if message.chat.id == SHIFT_CHANNEL:
        await client.send_message(SHIFT_CHANNEL,f'done bro')