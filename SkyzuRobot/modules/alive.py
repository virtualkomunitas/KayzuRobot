import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SkyzuRobot.events import register
from SkyzuRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/7d2fab979a7f4b5dd3af5.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kayzu Robot.** \n\n"
    TEXT += "♤ **I'm Working Properly** \n\n"
    TEXT += f"♤ **My Master : [Kayzu](https://t.me/Kayzuuuuu)** \n\n"
    TEXT += f"♤ **Library Version :** `{telever}` \n\n"
    TEXT += f"♤ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"♤ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/KayzuMusicBot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/KayzuSupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
