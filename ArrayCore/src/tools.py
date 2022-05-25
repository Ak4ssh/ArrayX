#ArrayCore 

import asyncio
import os
import sys

from natsort import natsorted
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from time import time
from .. import vcbot, SUDO_USERS, HNDLR, hl 
from dict.tools_dict import TOOL_DICT 


@vcbot.on_message(filters.command(["tools"], prefixes=HNDLR))
async def tools_(client: vcbot, e: Message):
    gid = e.chat.id
    bot_us = (await client.get_me()).username
    try:
        id_ = e.from_user.id
    except KeyError:
        await client.send_message(
            gid,
            text="**Click The Button Below To Get Tool Commands ⚙**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Tools", url=f"https://t.me/{bot_us}/?start=tools")]])
        )
        return
    buttons = tool_btns(id_)
    if gid==id_:
        await client.send_message(gid, text=TOOL, reply_markup=buttons)
    else:
        await client.send_message(
            gid,
            text="**Click The Button Below to get Tools Menu ⚙.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Tool", url=f"https://t.me/{bot_us}/?start=tools")]])
        )

        
@vcbot.on_callback_query(filters.regex(pattern=r"hlplist_(.*)"))
async def tool_list_parser(client: vcbot, cq: CallbackQuery):
    await cq.answer()
    user = cq.data.split("_")[1]
    buttons = tool_btns(user)
    await cq.edit_message_text(text=TOOL, reply_markup=buttons)


@vcbot.on_callback_query(filters.regex(pattern=r"tool_(.*)"))
async def tool_dicc_parser(client: vcbot, cq: CallbackQuery):
    await cq.answer()
    _, qry, user = cq.data.split("_")
    text = TOOL_DICT[qry]
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"hlplist_{user}")]])
    await cq.edit_message_text(text=text, reply_markup=btn, disable_web_page_preview=True)


def tool_btns(user):
    but_rc = []
    buttons = []
    hd_ = list(natsorted(TOOL_DICT.keys()))
    for i in hd_:
        but_rc.append(InlineKeyboardButton(i, callback_data=f"tool_{i}_{user}"))
        if len(but_rc)==2:
            buttons.append(but_rc)
            but_rc = []
    if len(but_rc)!=0:
        buttons.append(but_rc)
    return InlineKeyboardMarkup(buttons)
