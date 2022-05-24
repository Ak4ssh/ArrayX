import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v1"

APP_ID = int(os.getenv("APP_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
SESSION1 = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
HNDLR = os.getenv("HNDLR", "!")


def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list


sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [1517994352, 1789859817, 1432756163, 5136000092]
for x in DEVS:
    SUDO_USERS.append(x)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817 1432756163 5136000092").split())))
#----------------------------------------------

vcbot = Client(
    'ArrayCore',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'ArrayCore.vc'},
)

hl = HNDLR[0]
start_time = time.time()




#-------------------------CLIENTS-----------------------------
if SESSION:
    Session = Client(name="Venom1", api_id=API_ID, api_hash=API_HASH, session_string=SESSION1)
    call_py1 = PyTgCalls(Venom1)
else:
    Session = None
    call_py1 = None

if SESSION2:
    Session2 = Client(name="Venom2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
    call_py2 = PyTgCalls(Venom2)
else:
    Session2 = None
    call_py2 = None

if SESSION3:
    Session3 = Client(name="Venom3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
    call_py3 = PyTgCalls(Venom3)
else:
    Session3 = None
    call_py3 = None

if SESSION4:
    Session4 = Client(name="Venom4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
    call_py4 = PyTgCalls(Venom4)
else:
    Session4 = None
    call_py4 = None

if SESSION5:
    Session5 = Client(name="Venom5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
    call_py5 = PyTgCalls(Venom5)
else:
    Session5 = None
    call_py5 = None

if SESSION6:
    Session6 = Client(name="Venom6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6)
    call_py6 = PyTgCalls(Venom6)
else:
    Session6 = None
    call_py6 = None
        
if SESSION7:
    Session7 = Client(name="Venom7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7)
    call_py7 = PyTgCalls(Venom7)
else:
    Session7 = None
    call_py7 = None

if SESSION8:
    Session8 = Client(name="Venom8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8)
    call_py8 = PyTgCalls(Venom8)
else:
    Session8 = None
    call_py8 = None
