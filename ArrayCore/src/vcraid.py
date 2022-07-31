import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from Queue.queues import QUEUE, add_to_queue, get_queue, clear_queue

from .. import (Session, Session2, Session3, Session4, Session5)

from .. import (call_py1, call_py2, call_py3, call_py4,
                 call_py5, vcbot, HNDLR, SUDO_USERS)

logging.basicConfig(level=logging.INFO)

aud_list = [
    "./ArrayCore/resources/AUD1.mp3",
    "./ArrayCore/resources/AUD2.mp3",
    "./ArrayCore/resources/AUD3.mp3",
    "./ArrayCore/resources/AUD4.mp3",
    "./ArrayCore/resources/AUD5.mp3",
    "./ArrayCore/resources/AUD6.mp3",
    "./ArrayCore/resources/AUD7.mp3",
    "./ArrayCore/resources/AUD8.mp3",
    "./ArrayCore/resources/AUD9.mp3",
    "./ArrayCore/resources/AUD10.mp3",
    "./ArrayCore/resources/AUD11.mp3",
    "./ArrayCore/resources/AUD12.mp3",
    "./ArrayCore/resources/AUD13.mp3",
    "./ArrayCore/resources/AUD14.mp3",
    "./ArrayCore/resources/AUD15.mp3",
    "./ArrayCore/resources/AUD16.mp3",
    "./ArrayCore/resources/AUD17.mp3",
    "./ArrayCore/resources/AUD18.mp3",
    "./ArrayCore/resources/AUD19.mp3",
    "./ArrayCore/resources/AUD20.mp3",
]

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    aud = choice(aud_list)
    if inp:
        TheVenomXD = await e.reply_text("Initializing Clients For A Raid")
        link = f"https://itshellboy.tk/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py1:
                await Session.join_chat(chat_id)
                await call_py1.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
                await Session2.join_chat(chat_id)
                await call_py2.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
                await Session3.join_chat(chat_id)
                await call_py3.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
                await Session4.join_chat(chat_id)                      
                await call_py4.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
                await Session5.join_chat(chat_id)
                await call_py5.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream) 
            if call_py6:
                await Session6.join_chat(chat_id)
                await call_py6.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py7:
                await Session7.join_chat(chat_id)                      
                await call_py7.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py8:
                await Session8.join_chat(chat_id)
                await call_py8.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream) 
            if call_py9:
                await Session9.join_chat(chat_id)                      
                await call_py9.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py10:
                await Session10.join_chat(chat_id)
                await call_py10.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"> Raiding Started in: {chat_.title} \n\n> Audio: {songname} \n**> Position: Ongoing Raid")
            

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
async def raid(client, m: Message):
    gid = e.chat.id
    uid = e.from_user.id
    replied = m.reply_to_message
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
        if replied.audio or replied.voice:
            await m.delete()
            huehue = await replied.reply("**🔄 Processing**")
            TheVenomXD = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    songname = replied.audio.file_name[:35] + "..."
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, TheVenomXD, link, "Audio", 0)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/dda24d8a03f3d6a04afc6.jpg",
                    caption=f"""
** Added  {pos}
🏷️ Title: [{songname}]({link})
💬 Chat ID: {chat_id}
🎧 Requested by: {m.from_user.mention}**
""",
                )
            else:
                if call_py1:
                    await Session.join_chat(chat_id)
                    await call_py1.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py2:
                    await Session2.join_chat(chat_id)
                    await call_py2.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py3:
                    await Session3.join_chat(chat_id)
                    await call_py3.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py4:
                    await Session4.join_chat(chat_id)                      
                    await call_py4.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py5:
                    await Session5.join_chat(chat_id)
                    await call_py5.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream) 
                if call_py6:
                    await Session6.join_chat(chat_id)
                    await call_py6.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py7:
                    await Session7.join_chat(chat_id)                      
                    await call_py7.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py8:
                    await Session8.join_chat(chat_id)
                    await call_py8.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream) 
                if call_py9:
                    await Session9.join_chat(chat_id)                      
                    await call_py9.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                if call_py10:
                    await Session10.join_chat(chat_id)
                    await call_py10.join_group_call(chat_id, AudioPiped(TheVenomXD), stream_type=StreamType().pulse_stream)
                add_to_queue(chat_id, songname, TheVenomXD, link, "Audio", 0)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/dda24d8a03f3d6a04afc6.jpg",
                    caption=f"""
**▶ Started Raiding Audio File
🏷️ Title: [{songname}]({link})
💬 Chat ID: {chat_id}
🎧 Requested by: {m.from_user.mention}**
""",
                )

    else:
        if len(m.command) < 2:
            await m.reply("Reply to Audio File or provide something for Searching ...")
        else:
            await m.delete()
            huehue = await m.reply("🔎 Searching...")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await huehue.edit("`Didn't Find Anything for the Given Query`")
                
            
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            if call_py6:
                await call_py6.leave_group_call(chat_id)
            if call_py7:
                await call_py7.leave_group_call(chat_id)
            if call_py8:
                await call_py8.leave_group_call(chat_id)
            if call_py9:
                await call_py9.leave_group_call(chat_id)
            if call_py10:
                await call_py10.leave_group_call(chat_id)
            clear_queue(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            if call_py6:
                await call_py6.pause_stream(chat_id)
            if call_py7:
                await call_py7.pause_stream(chat_id)
            if call_py8:
                await call_py8.pause_stream(chat_id)
            if call_py9:
                await call_py9.pause_stream(chat_id)
            if call_py10:
                await call_py10.pause_stream(chat_id)    
            await e.reply_text(f"**VC Raid Paued In:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            if call_py6:
                await call_py6.resume_stream(chat_id)
            if call_py7:
                await call_py7.resume_stream(chat_id)
            if call_py8:
                await call_py8.resume_stream(chat_id)
            if call_py9:
                await call_py9.resume_stream(chat_id)
            if call_py10:
                await call_py10.resume_stream(chat_id)    
            await e.reply_text(f"**VC Raid Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No raid is currently paused!**")

