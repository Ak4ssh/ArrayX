# Array 


import asyncio
import re

from pyrogram import Client, filters
from pyrogram.types import Message

from . import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8,
               Session9, Session10, Session11, Session12,
               Session13, Session14, Session15, Session16,
               Session17, Session18, Session19, Session20,
               Session21, Session22, Session23, Session24,
               Session25, vcbot, hl)


ChatS = ["ArrayCore|RiZoeLXSpam|DNHxHELL|Array|Suzune"]
RiZ = ["@TheRiZoeL|@TheVenomXD|RiZoeL|Akash"]

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
async def spam(_, e: Message):
      gid = e.chat.id
      uid = e.from_user.id
      if gid == uid:
          Grp = await vcbot.ask(chat_id=message.chat.id, text="**Send Group Link Or Username Where You want to spam**")
          Group = Grp.text
          if "/cancel" in Group:
             return await e.reply_text("**All Process Cancelled**")
          if Group.startswith("https://t.me/") or Group.startswith("@"):
              if re.search(ChatS.lower(), Group.lower()):
                 await e.reply_text(("Sorry !! I can't Spam there")
              else:
                 await Session.join_chat(Group)
                 chat_ = await Session.get_chat(Group)
                 chat_id = chat_.id
          else:
              return await e.reply_text("**Send Group Link or Username**")
          Ans = await vcbot.ask(chat_id=message.chat.id, text="**Send Counts**")
          Num = Ans.text
          if "/cancel" in Num:
             return await e.reply_text("**All Process Cancelled**")
          if Num.isnumeric():
             count = int(Num)
          else:
             return await e.reply_text("Error! Send Counts in Numbers")
          Ask = await vcbot.ask(chat_id=message.chat.id, text="**Send Spam Message To Spam**")
          k = Ask.text
          if "/cancel" in k:
               return await e.reply_text("**All Process Cancelled**")
          if re.search(RiZ.lower(), k.lower()):
               return await e.reply_text(("Sorry !! I can't Spam on @Arraycore's Owner")
          Msgg = str(k)
          ids = 0
          try:
              if Session:
                   ids += 1
                   for _ in range(count):
                      await Session.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session2:
                   ids += 1
                   Session2.join_chat(Group)
                   for _ in range(count):
                      await Session2.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session3:
                   ids += 1
                   Session3.join_chat(Group)
                   for _ in range(count):
                      await Session3.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session4:
                   ids += 1
                   Session4.join_chat(Group)
                   for _ in range(count):
                      await Session4.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session5:
                   ids += 1
                   Session5.join_chat(Group)
                   for _ in range(count):
                      await Session5.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              await vcbot.send_message(e.chat.id, f"**Started Spam** \n\n **Group:** `{Group}` \n **IDs:** `{ids}` \n **Spam Message:** `{Msgg}`")

          except Exception as ex:
                  await vcbot.send_message(e.chat.id, f"Error: `{ex}`")
                  print(ex)  
