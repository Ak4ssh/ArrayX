from .. import hl

HELP_DICT = dict()

HELP_DICT["Music Player"] = f"""
**Basic music player commands!**

**Command:** `{hl}play`
**Usage:** __Plays the song in voice chat. Supports replied audio, Youtube link or just a keyword to search.__
**Example:** `{hl}play Closer`

**Command:** `{hl}end`
**Usage:** __Ends the music stream and leaves the voice chat.__

**Command:** `{hl}pause`
**Usage:** __Pause the music stream in voice chat.__

**Command:** `{hl}list`
**Usage:** __Shows the playlist in current chat.__

**Command:** `{hl}resume`
**Usage:** __Resumes the paused stream in voice chat.__

**Command:** `{hl}skip`
**Usage:** __Skips the current song playing in voice chat.__
"""

HELP_DICT["VC Raid"] = f"""
**Voice Chat Raiding Commands!**

**Command:** `{hl}raid`
**Usage:** __Raids the mentioned voice chat.__
**Example:**
    ~ `{hl}vcraid chat username/id` [If in bot PM.]
    ~ `{hl}vcraid` [If in a group.]

**Explanation:**
    ▪︎First Join All Your Id's In The Group By {hl}join `@chatusername` if chat is private Then {hl}join `https://t.me/+rNTg-asHGZYzODY1` \n Then Do {hl}raid In Groups 

**Command:** `{hl}raidend`
**Usage:** __Stops the voice chat raid and leaves voice chat.__

**Command:** `{hl}raidpause`
**Usage:** __Pauses the voice chat raid.__

**Command:** `{hl}raidresume`
**Usage:** __Resumes the paused voice chat raid.__
"""

HELP_DICT["Extras"] = f"""
**Some extra commands!**

**Command:** `{hl}help`
**Usage:** __To see the help menu with all command details.__

**Command:** `{hl}start`
**Usage:**  __To see the start message.__

**Command:** `{hl}join <username / invite link>`
**Usage:** __Joins the chat with all clients.__

**Command:** `{hl}leave <username> / <chat-id>`
**Usage:** __Leaves the chat with all clients.__
"""
