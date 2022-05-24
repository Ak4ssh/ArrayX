import asyncio

from pyrogram import idle

from . import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8,
               Session9, Session10, Session11, Session12,
               Session13, Session14, Session15, Session16,
               Session17, Session18, Session19, Session20,
               Session21, Session22, Session23, Session24,
               Session25, vcbot, hl)
               
from . import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8,            
               call_py9, call_py10, call_py11, call_py12,
               call_py13, call_py14, call_py15, call_py16,
               call_py17, call_py18, call_py19, call_py20,
               call_py21, call_py22, call_py23, call_py24,
               call_py25)


async def startup():
    # STARTING CLIENTS
    if Session:
        try:
            await Session.start()
            await Session.join_chat("ArrayCore")
            await Session.join_chat("RiZoeLX")
            await Session.join_chat("Its_Hellbot")
            await Session.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session2:
        try:
            await Session2.start()
            await Session2.join_chat("ArrayCore")
            await Session2.join_chat("RiZoeLX")
            await Session2.join_chat("Its_Hellbot")
            await Session2.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session3:
        try:
            await Session3.start()
            await Session3.join_chat("ArrayCore")
            await Session3.join_chat("RiZoeLX")
            await Session3.join_chat("Its_Hellbot")
            await Session3.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session4:
        try:
            await Session4.start()
            await Session4.join_chat("ArrayCore")
            await Session4.join_chat("RiZoeLX")
            await Session4.join_chat("Its_Hellbot")
            await Session4.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session5:
        try:
            await Session5.start()
            await Session5.join_chat("ArrayCore")
            await Session5.join_chat("RiZoeLX")
            await Session5.join_chat("Its_Hellbot")
            await Session5.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session6:
        try:
            await Session6.start()
            await Session6.join_chat("ArrayCore")
            await Session6.join_chat("RiZoeLX")
            await Session6.join_chat("Its_Hellbot")
            await Session6.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session7:
        try:
            await Session7.start()
            await Session7.join_chat("ArrayCore")
            await Session7.join_chat("RiZoeLX")
            await Session7.join_chat("Its_Hellbot")
            await Session7.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))

    if Session8:
        try:
            await Session8.start()
            await Session8.join_chat("ArrayCore")
            await Session8.join_chat("RiZoeLX")
            await Session8.join_chat("Its_Hellbot")
            await Session8.update_profile(bio="A Part Of @ArrayCore & @RiZoelX.") 
        except Exception as e:
            print(str(e))


    # STARTING BOT CLIENT
    await vcbot.start()
    get_me = await vcbot.get_me()
    usernamee = get_me.username
    msg = f"**My ArrayCore Deployed Successfully ✅ \n\n Bot Username :** @{usernamee} \n Hndlr : {hl}"
    if Session:
        await Session.join_chat("ArrayCoreLogs")
        await Session.send_message(-1001648072311, text=msg)
        await Session.leave_chat(-1001648072311)
    else:
        print("Error Occured Report This At @ArrayCoreChats")
        pass
  
    # STARTING ASSISTANTS
    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    
    # STARTUP COMPLETED
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
