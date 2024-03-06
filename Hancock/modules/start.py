import asyncio 
import random
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
)
from config import *
from pyrogram import filters
from Hancock import *
from Hancock.modules.games import *
from Hancock.database import *



# ----------------------------------------------------------------------------------------------  #
# --------------------------» ᴘʜᴏᴛᴏᴅ-sᴇᴄᴛɪᴏɴ «------------------------------------- #
photos = [
"https://telegra.ph/file/4e923543b7641fd46a429.jpg",
"https://telegra.ph/file/05cb8e48b29aeff809f22.jpg",
"https://telegra.ph/file/77d0f71ce0323a63e8b80.jpg",
"https://telegra.ph/file/0e100fe3757ac36495707.jpg",
"https://telegra.ph/file/3f3a0c5721b083712a443.jpg",
"https://telegra.ph/file/003b6081a3fc53bb32eb7.jpg",
"https://telegra.ph/file/4ea3049dc299a617d3a00.jpg",
"https://telegra.ph/file/66cb14b5821ffa80d1ffd.jpg",
"https://telegra.ph/file/aa6d76f7a901a8f06e5e4.jpg",
    
]



# ----------------------------------------------------------------------------------------------  #
# --------------------------» ᴛᴇxᴛ-sᴇᴄᴛɪᴏɴ «------------------------------------- #


START_TEXT = """**
ʜᴇʏ {}! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴍᴀᴢᴏɴ ʟɪʟʟʏ
ɴᴏʀᴍᴀʟʟʏ ᴘᴇᴏᴘʟᴇ ᴀʀᴇɴ'ᴛ ᴀʟʟᴏᴡᴇᴅ ʜᴇʀᴇ ᴇsᴘᴇᴄɪᴀʟʟʏ ᴍᴇɴ ʙᴜᴛ ɪ ᴄᴀɴ sᴇᴇ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴏғ ᴘᴜʀᴇ ʜᴇᴀʀᴛ,
 
ᴡʜᴏ ᴀᴍ ɪ ʏᴏᴜ ᴀsᴋ? Wᴇʟʟ ɪ ᴀᴍ ᴛʜᴇ ᴘɪʀᴀᴛᴇ ᴇᴍᴘʀᴇss ʙᴏᴀ ʜᴀɴᴄᴏᴄᴋ ᴛʜᴇ ᴍᴏsᴛ ʙᴇᴀᴜᴛɪғᴜʟ ʙᴏᴛ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ
Iғ ʏᴏᴜ ᴡɪsʜ ɴᴏᴛ ᴛᴏ ɢᴇᴛ ᴛᴜʀɴᴇᴅ ɪɴᴛᴏ sᴛᴏɴᴇ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ!
**"""

# ----------------------------------------------------------------------------------------------  #

HELP_TEXT = "**ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ɢᴜɪᴅᴇʟɪɴᴇs ᴏғ ʙᴏᴀ ʜᴀɴᴄᴏᴄᴋ**"

# ----------------------------------------------------------------------------------------------  #

H_T_P_TEXT = """
**sᴛᴀʀᴛ-ᴜᴘ ɢɪғᴛ:-**

• **ʏᴏᴜ ᴡɪʟʟ ᴏʙᴛᴀɪɴ** `500` **ᴛᴏᴋᴇɴs 🎴 ғᴏʀ sᴛᴀʀᴛ ᴜᴘ ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴜsᴇ ᴛʜᴇsᴇ ᴛᴏᴋᴇɴs ғᴏʀ** `/wager`
• **ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴇxᴛʀᴀ ʀᴏᴋᴇɴs 🎴 ʙʏ ᴄʜᴀᴛᴛɪɴɢ ᴏɴ** **[sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/TheNixaSupport)** **ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ ʏᴘᴜ sᴇɴᴛ ᴛʜᴇʀᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ** `+1` **ᴛᴏᴋᴇɴ**
• **ᴍᴏʀᴇ ᴏᴛʜᴇʀ ᴡᴀʏs ᴀʟsᴏ ᴛʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ᴛᴏᴋᴇɴs.**
"""

# ----------------------------------------------------------------------------------------------  #

ACCPT_1_TEXT = """ 
**ʜᴏᴡ ᴛᴏ ᴘʟᴀʏ :-**

• **ꜰɪʀꜱᴛ ʙᴇᴛ ʏᴏᴜʀ ᴛᴏᴋᴇɴꜱ ʙʏ ᴜꜱɪɴɢ** `/wager`
• **ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘᴏꜱɪᴛ ʏᴏᴜʀ ᴛᴏᴋᴇɴꜱ ᴛᴏ ʙᴀɴᴋ ʙʏ ᴜꜱɪɴɢ** `/deposit` 
• **ᴛᴏ ᴡɪᴛʜᴅʀᴀᴡ ʏᴏᴜʀ ᴛᴏᴋᴇɴꜱ ꜰʀᴏᴍ ʙᴀɴᴋ ᴜꜱᴇ** `/withdraw`
• **ʏᴏᴜ ᴄᴀɴ ɢɪꜰᴛ ʏᴏᴜʀ ᴛᴏᴋᴇɴꜱ ᴛᴏ ᴏᴛʜᴇʀ ᴘʟᴀʏᴇʀꜱ ʙʏ ᴜꜱɪɴɢ** `/present` 

**ɪᴍᴘᴏʀᴛᴀɴᴛ:-** `ᴘᴇʀ 15 ᴛɪᴍᴇꜱ ᴜꜱᴀɢᴇ ᴏꜰ /ᴡᴀɢᴇʀ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴠᴏɪᴅᴇᴅ ꜰᴏʀ 2 ᴍɪɴꜱ ᴡʜɪʟᴇ ᴛʜᴇꜱᴇ 2 ᴍɪɴꜱ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ /wager`

"""

# ----------------------------------------------------------------------------------------------  #

ACCPT_2_TEXT = """ 
**ʜᴏᴡ ᴛᴏ ᴜɴʟᴏᴄᴋ ɴᴇᴡ ʟᴇᴠᴇʟꜱ:-**

**ᴇᴠᴇʀʏ 50 ᴛɪᴍᴇꜱ ʏᴏᴜ ᴜꜱᴇ** `/wager` **ʏᴏᴜ ᴡɪʟʟ ʟᴇᴠᴇʟ ᴜᴘ**

**ꜰᴏʀ ᴇxᴀᴍᴘʟᴇ:**
• **50 ᴛᴏᴛᴀʟ ᴘʟᴀʏꜱ =** `ʟᴠʟ 1 = 1000 xᴘ ʙᴏɴᴜꜱ`
• **200 ᴛᴏᴛᴀʟ ᴘʟᴀʏꜱ =** `ʟᴠʟ 2 = 2000 xᴘ ʙᴏɴᴜꜱ`

**ɴᴏᴛᴇ:-** `ꜰᴏʀ ᴇᴠᴇʀʏ ɴᴇᴡ ʟᴇᴠᴇʟ - ʏᴏᴜ ᴄᴀɴ ᴜɴʟᴏᴄᴋ ʀᴀɴᴅᴏᴍ ᴘʀɪᴍɪᴜᴍ ʟᴏᴏᴛ ʙᴏx | ʀᴀʀᴇ ɪᴛᴇᴍꜱ ᴀʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴘʀᴇᴍɪᴜᴍ ɢɪꜰᴛ ʙᴏx `
"""

# ----------------------------------------------------------------------------------------------  #

ACCPT_3_TEXT = """ 
**ʜᴏᴡ ᴛᴏ ᴠɪᴇᴡ ᴀɴᴅ ᴇᴅɪᴛ ʏᴏᴜʀ ᴘʀᴏꜰɪʟᴇ/ꜱᴛᴀᴛꜱ:-**

• `/profile` - **ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴏꜰɪʟᴇ/ꜱᴛᴀᴛꜱ/ᴛᴏᴋᴇɴꜱ**
• `/setprofile` - **ꜱᴇᴛ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄ** `[ʟᴠʟ 1 ʀᴇQᴜɪʀᴇᴅ] [1000 ᴛᴏᴋᴇɴꜱ ʀᴇQᴜɪʀᴇᴅ]`
• `/shop` - **ᴛᴏ ʙᴜʏ ɪᴛᴇᴍꜱ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴏᴋᴇɴꜱ | ᴇᴠᴇʀʏ ᴅᴀʏ ᴀ ɴᴇᴡ ᴡᴀɪꜰᴜ/ʜᴜꜱʙᴀɴᴅᴏ ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ɪᴛᴇᴍꜱ ᴡɪʟʟ ʙᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴘᴜʀᴄʜᴀꜱᴇ**
• `/items` - **ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴘᴜʀᴄʜᴀꜱᴇᴅ ɪᴛᴇᴍꜱ**
• `/data` - **ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀ ᴏꜰ ʏᴏᴜʀ ᴜɴɪQᴜᴇ'ꜱ ɪᴅꜱ**
• `/leaderboard` - **ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 10 ᴘʟᴀʏᴇʀꜱ**

**ɴᴏᴛᴇ:-** `ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ ɪꜱ ꜱᴏʀᴛᴇᴅ ʙʏ ᴛᴏᴋᴇɴꜱ ɴᴏᴛ ʙʏ ʟᴇᴠᴇʟ ᴏʀ ᴛᴏᴛᴀʟ ᴘʟᴀʏꜱ`

"""

# ----------------------------------------------------------------------------------------------  #

WAGER_TEXT = """ 
**ᴜsᴀɢᴇ ᴏғ ᴡᴀɢᴇʀ:-**

• `/wager` **ɪs ᴛʜᴇ ᴍᴀɪɴ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇᴅ ᴛᴏ ʙᴇᴛ ᴏɴ ᴛʜɪs ʙᴏᴛ.**

**ɴᴏᴛᴇ:-** `sᴏᴍᴇᴛɪᴍᴇs ʏᴏᴜ ᴡɪʟʟ ᴡᴏɴ ᴛᴏᴋᴇɴs sᴏᴍᴇᴛɪᴍᴇs ʏᴏᴜ ᴡɪʟʟ ʟᴏsᴇ ʏᴏᴜ ᴛᴏᴋᴇɴs ɪᴛ ᴅᴇᴘᴇɴᴅs ᴏɴ ʏᴏᴜʀ ʟᴜᴄᴋ.`
**ɪᴍᴘᴏʀᴛᴀɴᴛ:-** `ᴘᴇʀ 15 ᴛɪᴍᴇs ᴜsᴀɢᴇ ᴏғ /wager ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴠᴏɪᴅᴇᴅ ғᴏʀ 2 ᴍɪɴs ᴡʜɪʟᴇ ᴛʜᴇsᴇ 2 ᴍɪɴs ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ /wager.`
"""

# ----------------------------------------------------------------------------------------------  #

RESET_TEXT = """ 
**ᴜsᴀɢᴇ ᴏғ ʀᴇsᴇᴛ:-**

• `/reset` **ɪs ᴛʜᴀ ᴍᴀɪɴ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇᴅ ᴛᴏ ʀᴇsᴇᴛ ʏᴏᴜʀ ᴅᴀᴛᴀʙᴀsᴇ ᴏɴ ᴛʜɪs ʙᴏᴛ**

**ɴᴏᴛᴇ:-** `ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇsᴇᴛ ᴊᴜsᴛ ᴄᴏʟʟᴇᴄᴛ 1000 ᴛᴏᴋᴇɴs ᴛᴏ ʀᴇsᴇᴛ ᴀɴᴅ sᴛᴀʀᴛ ᴀɢᴀɪɴ ɴᴇᴡ.`
"""

# ----------------------------------------------------------------------------------------------  #

PROFILE_HELP_TEXT = """ 
**ᴜsᴀɢᴇ ᴏғ ᴘʀᴏғɪʟᴇ:-**

• `/profile` - **ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ/sᴛᴀᴛs/ᴛᴏᴋᴇɴs.**
• `/setprofile` - **sᴇᴛ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍɪsᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ.** `[ʟᴠʟ 1 ʀᴇǫᴜɪʀᴇᴅ]`

"""

# ----------------------------------------------------------------------------------------------  #

SHOP_HELP_TEXT = """ 
**ʜᴏᴡ ᴛᴏ sʜᴏᴘ:-**

• `/shop` - **ᴛᴏ ʙᴜʏ ɪᴛᴇᴍs ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴏᴋᴇɴs | ᴇᴠᴇʀʏ ᴅᴀʏ ᴀ ɴᴇᴡ ᴡᴀɪғᴜ/ʜᴜsʙᴀɴᴅᴏ ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀs ɪᴛᴇᴍs ᴡɪʟʟ ʙᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴘᴜʀᴄʜᴀsᴇ.**
• `/items` - **ᴛᴏ ᴠɪᴇᴡs ʏᴏᴜʀ ᴘᴜʀᴄʜᴀsᴇ ɪᴛᴇᴍs.**
• `/data` - **ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀ ᴏғ ʏᴏᴜʀ ᴜɴɪǫᴜᴇ's ɪᴅs**

"""

# ----------------------------------------------------------------------------------------------  #

BANK_HELP_TEXT = """ 
**ᴜsᴀɢᴇ ᴏғ ʙᴀɴᴋ ᴀɴᴅ ɢɪғᴛ:-**

• `/withdraw` - **ᴡɪᴛʜᴅʀᴀᴡ ʏᴏᴜʀ ᴛᴏᴋᴇɴs ғʀᴏᴍ ʙᴀɴᴋ.**
• `/deposit` - **ᴅᴇᴘᴏsɪᴛᴇ ʏᴏᴜʀ ᴛᴏᴋᴇɴs ᴛᴏ ʏᴏᴜʀ ʙᴀɴᴋ ᴀᴄᴄᴏᴜɴᴛ.**

**ɢɪғʏ ʏᴏᴜʀ ᴛᴏᴋᴇɴs:-**

• `/present` - **ʏᴏᴜ ᴄᴀɴ ɢɪғᴛ ʏᴏᴜʀ ᴛᴏᴋᴇɴs ᴛᴏ ᴏᴛʜᴇʀ ᴘʟᴀʏᴇʀs.**

"""

# ----------------------------------------------------------------------------------------------  #

LEADERBOARD_HELP_TEXT = """ 
**ᴜsᴀɢᴇ ᴏғ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ:-**

• `/Leaderboard` - **ᴛᴏ ɢᴇᴛ ɢʟᴏʙᴀʟ ᴛᴏᴘ ᴛᴇɴ ᴘʟᴀʏᴇʀs**

**ɴᴏᴛᴇ:-** `ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ ɪs sᴏʀᴛᴇᴅ ʙʏ ᴛᴏᴋᴇɴs ɴᴏᴛ ʙʏ ʟᴇᴠᴇʟ ᴏʀ ᴛᴏᴛᴀʟ ᴘʟᴀʏs.`

"""

# ----------------------------------------------------------------------------------------------  #
# --------------------------» ʙᴜᴛᴛᴏɴs-sᴇᴄᴛɪᴏɴ «------------------------------------- #


START_BUTTON = [[
        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
    ],
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 🗡️", url="https://t.me/TheNixaSupport"),
        InlineKeyboardButton("ʜᴇʟᴘ 🛡️", callback_data="help_callback") 
    ]]

# ----------------------------------------------------------------------------------------------  #

HELP_BUTTON = [
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴘʟᴀʏ", callback_data="H_T_P"),
        ],
        [
            InlineKeyboardButton("ᴡᴀɢᴇʀ", callback_data="Wager_Button"),
            InlineKeyboardButton("ᴘʀᴏғɪʟᴇ", callback_data="Profile_Button"),
        ],
        [
            InlineKeyboardButton("sʜᴏᴘ", callback_data="Shop_Button"),
            InlineKeyboardButton("ʙᴀɴᴋ", callback_data="Bank_Button"),
        ],
        [
            InlineKeyboardButton("ʟᴇᴅᴇʀʙᴏᴀʀᴅ", callback_data="LeaderBoard_Button"),
            InlineKeyboardButton("ʀᴇsᴇᴛ", callback_data="Re_Button"),
        ],
        [
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="delete"),
        ]]

# ----------------------------------------------------------------------------------------------  #

H_T_P_BUTTON = [[
            InlineKeyboardButton("ɴᴇxᴛ", callback_data="Accept_1"),
              ]]

# ----------------------------------------------------------------------------------------------  #

ACCPT_1_BUTTON = [[
            InlineKeyboardButton("ɴᴇxᴛ", callback_data="Accept_2"),
                 ]]

# ----------------------------------------------------------------------------------------------  #

ACCPT_2_BUTTON = [[
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Accept_1"),
            InlineKeyboardButton("ɴᴇxᴛ", callback_data="Accept_3"),
                 ]]

# ----------------------------------------------------------------------------------------------  #

ACCPT_3_BUTTON = [[
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Accept_2"),
            InlineKeyboardButton("ɴᴇxᴛ", callback_data="Help_Back"),
                 ]]

# ----------------------------------------------------------------------------------------------  #

HELP_BACK_BUTTON = [[
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Help_Back"),
                   ]]

# ----------------------------------------------------------------------------------------------  #

PHELP_BUTTON = [[
            InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ", url=f"https://telegram.me/{BOT_USERNAME}?start=help"),
               ]]


# ----------------------------------------------------------------------------------------------  #
PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
# ----------------------------------------------------------------------------------------------  #



# ----------------------------------------------------------------------------------------------  #
# --------------------------» ғᴜɴᴄᴛɪᴏɴ-sᴇᴄᴛɪᴏɴ «------------------------------------- #


@Hancock.on_message(filters.command(["start"], PREFIX))
async def start(_, message):
    money = await get_player_xp(message.from_user.id)

    if len(message.command) > 1:
        if startCheckQuery(message, StartQuery='abcdefghijkmnop1234'):
            us_in_db = await get_player(message.from_user.id)             
            if not us_in_db:
                return await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ᴇᴠᴇᴍ ɴᴏᴛ ᴘʟᴀʏᴇᴅ ᴀ sɪɴɢʟᴇ ᴡᴀɢᴇʀ!\n\nᴘʟᴀʏ ғɪʀsᴛ ʙʏ ᴜsɪɴɢ /wager ᴏɴ ɢʀᴏᴜᴘ ᴜsᴇᴅ ᴛʜᴇ ʟɪɴᴋ.`")
            if message.from_user.id in (await get_got_id()):
                return await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ ᴛʜɪs ʟɪɴᴋYou 🖇️`")
            else:
                hehe = money + 1000
                await update_player_xp(message.from_user.id, hehe)
                await add_got(message.from_user.id, "abcdefghijkmnop1234")
                await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ɢᴏᴛ 1000 🎴 `")
        if startCheckQuery(message, StartQuery='help'):
                await message.reply_photo(photo=random.choice(photos), caption=HELP_TEXT,
                                         reply_markup=InlineKeyboardMarkup(HELP_BUTTON))
    else:
        await message.reply_photo(photo=random.choice(photos), caption=START_TEXT.format(message.from_user.mention),
                             reply_markup=InlineKeyboardMarkup(START_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_message(get_command("help"))
async def _help(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply_photo(photo=random.choice(photos), caption=HELP_TEXT,
                                  reply_markup=InlineKeyboardMarkup(HELP_BUTTON))
    if not message.chat.type == enums.ChatType.PRIVATE:
       return await message.reply_text("**ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ ʜᴇʟᴘ ɢᴜɪᴅᴇʟɪɴᴇs**",
                                  reply_markup=InlineKeyboardMarkup(PHELP_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("help_callback"))
async def help(client, query):
    await query.message.reply_photo(photo=random.choice(photos), caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))
# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("Help_Back"))
async def helpback(client, query):
    await query.edit_message_caption(HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("H_T_P"))
async def how_to_play(_, query: CallbackQuery):
    await query.edit_message_caption(H_T_P_TEXT,
       reply_markup=InlineKeyboardMarkup(H_T_P_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("Accept_1"))
async def accpt_1(_, query: CallbackQuery):
    await query.edit_message_caption(ACCPT_1_TEXT,
       reply_markup=InlineKeyboardMarkup(ACCPT_1_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("Accept_2"))
async def accpt_2(_, query: CallbackQuery):
    await query.edit_message_caption(ACCPT_2_TEXT,
       reply_markup=InlineKeyboardMarkup(ACCPT_2_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("Accept_3"))
async def accpt_3(_, query: CallbackQuery):
    await query.edit_message_caption(ACCPT_3_TEXT,
       reply_markup=InlineKeyboardMarkup(ACCPT_3_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("Wager_Button"))
async def wager(_, query: CallbackQuery):
    await query.edit_message_caption(WAGER_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("Re_Button"))
async def reset_help(_, query: CallbackQuery):
    await query.edit_message_caption(RESET_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("Profile_Button"))
async def profile_help(_, query: CallbackQuery):
    await query.edit_message_caption(PROFILE_HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("Shop_Button"))
async def shop_help(_, query: CallbackQuery):
    await query.edit_message_caption(SHOP_HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("Bank_Button"))
async def bank_help(_, query: CallbackQuery):
    await query.edit_message_caption(BANK_HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #
 
@Hancock.on_callback_query(filters.regex("LeaderBoard_Button"))
async def Leaderboard_help(_, query: CallbackQuery):
    await query.edit_message_caption(LEADERBOARD_HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON))

# ----------------------------------------------------------------------------------------------  #

@Hancock.on_callback_query(filters.regex("delete"))
async def delete(_, query):    
    await query.message.delete()

# ----------------------------------------------------------------------------------------------  #

