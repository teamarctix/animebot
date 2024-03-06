import datetime
import random
import asyncio 
import pymongo
import requests as r 
import json

from Hancock import *
from Hancock.database import *
from pyrogram import *
from pyrogram.types import *
from telegraph import upload_file
from bs4 import BeautifulSoup as bs
from config import SUDO_USERS as s

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



hek = [6109551937, 5917071362]
babe = [x*50 for x in range(1, 500)]
textbabe = """
**🛍 ɴᴇᴡ ᴅᴀɪʟʏ sʜᴏᴘ! 🛍**

**ɴᴀᴍᴇ:** `{}` **(**`{}`**)**
**ᴘʀɪᴄᴇ:** `{}` **🎴**

**ʏᴏᴜʀ ᴛᴏᴋᴇɴ:** `{}` 🎴
"""

async def total_items_value(user_id: int):
    db = []
    x = await get_boughts(user_id)
    if not x:
        return 0
    y = x.split(",")
    for x in y:
        m = await get_shop(int(x))
        k = m["value"]
        db.append(int(k))
    return(int(sum(db)))

@Hancock.on_callback_query(filters.regex("backp"))
async def _backp(client, query):
  user_id = int(query.data.split(":")[1])
  if not query.from_user.id == user_id:
    return await query.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴘʟᴀʏᴇʀ", show_alert=True)         
  else:
      await query.message.delete()
      b = await get_player_bank(query.from_user.id)
      x = await get_player_level(query.from_user.id)
      y = await get_player_xp(query.from_user.id)
      z = await get_player_profile(query.from_user.id)
      t = await get_player_total(query.from_user.id)
      p = (int(x)+1)*50
      d = await get_boughts(query.from_user.id)
      uwu = await total_items_value(query.from_user.id)
      if z == None and d:
          return await query.message.reply_photo(photo=random.choice(photos), caption=f"""
**🎮 {query.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍs ᴠᴀʟᴜᴇ:** `{uwu}`
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ɪᴛᴇᴍs 🛒",callback_data=f"items:{query.from_user.id}")]]))
      elif z == None and not d:
          return await query.message.reply_photo(photo=random.choice(photos), caption=f"""
**🎮 {query.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍs ᴠᴀʟᴜᴇ:** `{uwu}`
""")
      elif z: 
          return await query.message.reply_photo(z, caption=f"""
**🎮 {query.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍs ᴠᴀʟᴜᴇ:** `{uwu}`
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ɪᴛᴇᴍs 🛒",callback_data=f"items:{query.from_user.id}")]]))


@Hancock.on_callback_query(filters.regex("items"))
async def _(client, query):
    user_id = int(query.data.split(":")[1])
    if not query.from_user.id == user_id:
        return await query.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴘʟᴀʏᴇʀ", show_alert=True)         
    else:
        x = await get_boughts(user_id)
        y = x.split(",")
        num = 0
        textt = f"{query.from_user.mention}**'s ɪᴛᴇᴍs**\n\n"
        textt += "".join(f"`{y.index(m) + 1}`. `{m}`\n" for m in y)
        textt += "\n**ɴᴏᴛᴇ:-** `ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴜɴɪǫᴜᴇ ɪᴅ ᴏғ ʏᴏᴜʀ ɪᴛᴇᴍs ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ɪᴅs ᴛᴏ sᴀʟᴇ ᴏʀ ɢɪᴠᴇ ʏᴏᴜʀ ɪᴛᴇᴍs ᴛᴏ ᴀɴʏ ᴏᴛʜᴇʀ ᴘʟᴀʏᴇʀs ᴛᴏ ɢᴇᴛ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ɪᴅ ᴜsᴇ /data ɪᴅ (ʙᴇᴛᴀ ᴛᴇsᴛɪɴɢ).`"
        return await query.message.edit_media(media=InputMediaPhoto("https://graph.org/file/84d224c4a46e1b2e79a9b.jpg", caption=textt), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Back ◀️",callback_data=f"backp:{user_id}")]]))

@Hancock.on_callback_query(filters.regex(r'stop'))
async def _(client, query):
    # This will return response None at listen
    await client.listen.Cancel(filters.user(query.from_user.id))
    
@Hancock.on_message(get_command("guess") & ~filters.private)
async def guess(client, message):
  #await message.reply_text("`ᴄᴜʀʀᴇɴᴛʟʏ ᴅɪsᴀʙʟᴇᴅ.`")
  soup = bs(r.get('https://mywaifulist.moe/random').text, 'html.parser')
  mything = json.loads(soup.find('div', attrs={'id': 'app'}).get('data-page'))['props']['waifu']
  hehe = mything["name"]
  huh = hehe.replace("(", "")
  lmao = huh.replace(")", "")
  fuck = lmao.replace("Husbando", "")
  uwu = fuck.lower()
  m = await message.reply_photo(mything['display_picture'], caption='**ɢᴜᴇss ᴛʜᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ғᴏʀ** `250` **ᴄᴏɪɴs**')
  us_in_db = await get_player(message.from_user.id)            
  if not us_in_db:
      return await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ᴇᴠᴇɴ ɴᴏᴛ ᴘʟᴀʏᴇᴅ ᴀ sɪɴɢʟᴇ ᴡᴀɢᴇʀ!`")
  else:
      return await add_message(uwu, m.id)

def startCheckQuery(message, StartQuery=None) -> bool:
    if (
        StartQuery in message.command[1].split('_')[0]
        and message.command[1].split('_')[0] == StartQuery
    ):
        return True
    else: 
        return False 

async def make_shop(message, pic: str, name: str, series: str, value: int, token: int, final: int):
       await message.reply_photo(pic, caption=textbabe.format(name, series, value, token), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ʙᴜʏ {name} ғᴏʀ {value} 🎴",callback_data=f"buy:{message.from_user.id}:{final}")]]))

@Hancock.on_message(get_command("leaderboard"))
async def _leaderboard(_, message):
    point = db.players.find().sort("xp", pymongo.DESCENDING)
    points = await point.to_list(10)
    texto = "**📈 GLOBAL LEADERBOARD | 🌍**\n\n"
    num = 0
    for x in points:
        num += 1
        try:
            users = await bot.get_users(x['player'])
            userss = users.first_name
        except Exception:
            userss = x["player"]  
        texto += f"`{num}`. **{userss}** [**ʟᴠ:** `{x['level']}`] [**xᴘ:** `{x['xp']}`]\n"
    await message.reply_photo(photo=random.choice(photos), caption=texto)

@Hancock.on_message(wager_command("wager") & ~filters.private)
async def _wager(_, message):
  us_in_db = await get_player(message.from_user.id)   
  if not us_in_db:
    await add_player(message.from_user.id, 500, 0, 0, 0)
    return await message.reply_photo(photo=random.choice(photos), caption="**ᴡᴇʟᴄᴏᴍᴇ ɴᴇᴡ ᴘʟᴀʏᴇʀ**\n\n**ʏᴏᴜ ɢᴏᴛ** `500` 🎴 **ᴛᴏᴋᴇɴ ғᴏʀ sᴛᴀʀᴛ-ᴜᴘ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴛᴏᴋᴇɴs ᴛᴏ ᴡᴀɢᴇʀ.**")
  result = ["True", "False"]
  final = random.choice(result) 
  money = await get_player_xp(message.from_user.id)
  total = await get_player_total(message.from_user.id)
  if len(message.command) < 2:
      return await message.reply_text("`ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ᴡᴀɢᴇʀ.`")          
  else:
    wager = message.text.split()[1]
    if not str(wager).isdigit() or int(wager) > money or int(wager) == 0:
      return await message.reply_text("`ʏᴏᴜʀ ᴠᴀʟᴜᴇ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.`")
    if final == "True":
      total = total + 1
      money = money + int(wager)
      await update_player_xp(message.from_user.id, money)
      await update_player_total(message.from_user.id, total)
      await message.reply_text(f"{message.from_user.mention} **ʜᴀs ᴡᴀɢᴇʀ** `{str(wager)}` **ᴛᴏᴋᴇɴs 🎴**\n\n**ᴡᴇᴡ! ʏᴏᴜ ʜᴀᴠᴇ ɢᴀɪɴ** `{str(wager)}` **ᴛᴏᴋᴇɴs (✅)**")
    else:
      total = total + 1
      money = money - int(wager)
      await update_player_xp(message.from_user.id, money)
      await update_player_total(message.from_user.id, total)
      await message.reply_text(f"{message.from_user.mention} **ʜᴀs ᴡᴀɢᴇʀ** `{str(wager)}` **ᴛᴏᴋᴇɴs 🎴**\n\n**ᴏᴏᴘs! ʏᴏᴜ ʜᴀᴠᴇ ᴅʀᴏᴘ** `{str(wager)}` **ᴛᴏᴋᴇɴs (❌)**")
    if total in babe:
        try:
            ok = int(total/50)
            money = money + int(ok*1000)
            await message.reply_photo(photo=random.choice(photos), caption=f"**⚔️ ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs** {message.from_user.mention} **ғᴏʀ ʀᴇᴀᴄʜɪɴɢ ᴛʜᴇ ʟᴇᴠᴇʟ {ok}**\n\n**ʏᴏᴜ ʜᴀᴠᴇ ᴏʙᴛᴀɪɴ:** `{int(ok*1000)}` **ᴛᴏᴋᴇɴs 🎴**")
            await update_player_level(message.from_user.id, ok)
            await update_player_xp(message.from_user.id, money)
        except Exception as e:
            print(e)

@Hancock.on_message(get_command("present") & ~filters.private)
async def _present(_, message):
  if not message.reply_to_message or message.reply_to_message.from_user.id == message.from_user.id:
    return await message.reply_text("`ʀᴇᴘʟʏ sᴏᴍᴇᴏɴᴇ ᴛᴏ ᴘʀᴇsᴇɴᴛ.`")
  if not len(message.command) < 2:
    amount = message.text.split()[1]
  else:
    return await message.reply_text("`ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ᴘʀᴇsᴇɴᴛ.`")
  reply = message.reply_to_message.from_user
  money = await get_player_xp(reply.id)
  gone = await get_player_xp(message.from_user.id)
  us_in_db = await get_player(reply.id)
  if not us_in_db:
    return await message.reply_text("`ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟɪᴇᴅ ᴀ ᴜsᴇʀ ᴡʜᴏ ᴡᴀs ɴᴏᴛ ᴡᴀɢᴇʀ ᴀ sɪɴɢʟᴇ ᴛɪᴍᴇ.`")
  else:
      if not str(amount).isdigit() or int(amount) > gone or int(amount) == 0:
        return await message.reply_text("`ʏᴏᴜʀ ᴘʀᴇsᴇɴᴛ ᴀᴍᴏᴜɴᴛ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ`")
      else:
        present = money + int(amount)
        went = gone - int(amount)
        await update_player_xp(message.from_user.id, went)
        await update_player_xp(reply.id, present)
        return await message.reply_text("**ʏᴏᴜ ʜᴀᴠᴇ ᴘʀᴇsᴇɴᴛᴇᴅ: **" + f"`{str(amount)}` 🎴 " + f"**ᴛᴏ** {reply.mention}" + "\n\n" f"**ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ:** `{went}`")

@Hancock.on_message(get_command("setprofile"))
async def _setprofile(_, message):
  us_in_db = await get_player(message.from_user.id)             
  if not message.reply_to_message or not message.reply_to_message.media:
    return await message.reply_text("`ʀᴇᴘʟʏ ᴛᴏ ᴀᴇᴅɪᴀ sᴇᴛ ᴀs ᴘʀᴏғɪʟᴇ.`")
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ sᴇᴛ ᴛʜᴇɪʀ ᴘʀᴏғɪʟᴇ`")
  else:
      k = await get_player_level(message.from_user.id)
      if k < 1:
          try:
              path = await message.reply_to_message.download()
              telegraph = upload_file(path)
              for file_id in telegraph:
                    ido = file_id
          except Exception as e:
                    print(e)
                    return await message.reply_text("**ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ sɪᴢᴇ ᴏғ ᴛʜᴇ ғɪʟᴇ ᴍᴜsᴛ ʙᴇ ᴜɴᴅᴇʀ ʙ ᴛᴏ sᴇᴛ ᴀs ᴘʀᴏғɪʟᴇ.**")             
          await message.reply_photo(photo=random.choice(photos), caption=f"**ᴛᴏ sᴇᴛ ᴛʜɪs ᴀs ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ʏᴏᴜ ᴍᴜsᴛ ᴏɴ ʟᴇᴠᴇʟ 1 ʙᴜᴛ ʏᴏᴜʀ ʟᴇᴠᴇʟ ɪs {k}**")
      else: 
          try:
              path = await message.reply_to_message.download()
              telegraph = upload_file(path)
              for file_id in telegraph:
                    ido = file_id
          except Exception as e:
                    print(e)
                    return await message.reply_text("**ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ sɪᴢᴇ ᴏғ ᴛʜᴇ ғɪʟᴇ ᴍᴜsᴛ ʙᴇ ᴜɴᴅᴇʀ 5ᴍʙ ᴛᴏ sᴇᴛ ᴀs ᴘʀᴏғɪʟᴇ.**")             
          await message.reply_photo(f"https://graph.org{ido}", caption="**ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴛ ᴛʜɪs ᴀs ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ.**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sᴇᴛ ᴘʀᴏғɪʟᴇ ғᴏʀ 100 🎴",callback_data=f"set:{message.from_user.id}:{ido}")]]))

@Hancock.on_message(get_command("rob"))
async def _rob(_, message):
  current_date = datetime.datetime.now()
  final = current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000
  us_in_db = await get_player(message.from_user.id)  
  if not message.reply_to_message:
    return await message.reply_text("`ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʟᴀʏᴇʀ.`")
  if message.reply_to_message.from_user.id == message.from_user.id:
    return await message.reply_text("`ɢᴏɴɴᴀ ʀᴏʙ ʏᴏᴜʀsᴇʟғ ?`")
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ʀᴏʙ.`")
  rus_in_db = await get_player(message.reply_to_message.from_user.id)             
  if not rus_in_db:
    return await message.reply_text("`ʏᴏᴜ ʀᴇᴘʟɪᴇᴅ ᴀ ᴜsᴇʀ ᴡʜᴏ ʜᴀᴠᴇ ɴᴏᴛ ᴅᴏɴᴀ ᴀ sɪɴɢʟᴇ ᴡᴀɢᴇʀ.`")
  else:
      k = await get_player_level(message.from_user.id)
      x = await get_player_level(message.reply_to_message.from_user.id)
      xp = await get_player_xp(message.from_user.id)
      rxp = await get_player_xp(message.reply_to_message.from_user.id)
      if k < 5:
          return await message.reply_text("`ᴛᴏ ᴀ ᴘʟᴀʏᴇʀ ʏᴏᴜ ᴍᴜsᴛ ᴏɴ ʟᴇᴠᴇʟ 5+`")
      if x < 1:
          return await message.reply_text("`ᴛᴏ ʀᴏʙ ᴀ ᴘʟᴀʏᴇʀ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴘʟᴀʏᴇʀ ᴍᴜsᴛ ᴏɴ ʟᴇᴠᴇʟ 1+`")
      if rxp < 500:
          return await message.reply_text("`ᴛᴘ ʀᴏʙ ᴀ ᴘʟᴀʏᴇʀ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴘʟᴀʏᴇʀ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ 500+ ᴛᴏᴋᴇɴs 🎴`")
      else:
          await add_robs(final, message.from_user.id)  
          bb = await get_robs(final, message.from_user.id)         
          result = ["True", "False"]
          final = random.choice(result) 
          lose = random.randint(500, rxp)
          if bb == 5:
              return await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ʀᴇᴀᴄʜᴇᴅ ᴍᴀx ʀᴏʙs ᴛᴏᴅᴀʏ.`")
          if final == "True":
              sad = rxp - lose
              total = xp + lose
              gtfko = bb + 1
              remaining = 5 - bb
              await update_player_xp(message.from_user.id, total)
              await update_player_robs(final, message.from_user.id, gtfko)
              await update_player_xp(message.reply_to_message.from_user.id, sad)
              await message.reply_text(f"{message.from_user.mention} **ʜᴀᴠᴇ ᴛʀɪᴇᴅ ᴛᴏ ʀᴏʙ** {message.reply_to_message.from_user.mention} **ᴀɴᴅ ᴛᴏᴏᴋ ᴀᴡᴀʏ** `{lose}` **(✅)**\n\n**ʀᴏʙʙᴇʀɪᴇs ʀᴇᴍᴀɪɴɪɴɢ:** `{remaining}`")
          if final == "False":
              await message.reply_text(f"{message.from_user.mention} **ʜᴀᴠᴇ ᴛʀɪᴇᴅ ᴛᴏ ʀᴏʙ** {message.reply_to_message.from_user.mention} **ʙᴜᴛ ᴘʟᴏɪᴄᴇ ʜᴀᴠᴇ ᴄᴀᴜɢʜᴛ ʜɪᴍ (🚨)**")
              await message.reply_text(f"**ᴊᴜsᴛ ᴍɪss** {message.from_user.mention} **ʜᴀᴠᴇ ᴇsᴄᴀᴘᴇᴅ ғʀᴏᴍ ᴘᴏʟɪᴄᴇ ʙᴜᴛ ɴᴏ ᴍᴏʀᴇ ʀᴏʙʙᴇʀɪᴇs ᴛᴏᴅᴀʏ (❌)**")
              await update_player_robs(final, message.from_user.id, 5)
          
@Hancock.on_message(get_command("reset"))
async def _reset(_, message):
  us_in_db = await get_player(message.from_user.id)             
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ʀᴇsᴇᴛ`")
  else:
    await message.reply_text("**ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ʀᴇsᴇᴛ ʏᴏᴜʀ ᴅᴀᴛᴀʙᴀsᴇ**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʀᴇsᴇᴛ ғᴏʀ 1000 🎴",callback_data=f"reset:{message.from_user.id}")]]))

@Hancock.on_callback_query(filters.regex("reset"))
async def reset(_, query):
     user_id = int(query.data.split(":")[1])
     xp = await get_player_xp(query.from_user.id)
     if not query.from_user.id == user_id:
         return await query.answer("ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴘʟᴀʏᴇʀ ᴡʜᴏ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛᴏ ʀᴇsᴇᴛ", show_alert=True)         
     if xp < 1000:
         return await query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴛᴏᴋᴇɴ ᴛᴏ ʀᴇsᴇᴛ", show_alert=True)
     else:
        await db.players.delete_one({"player": user_id})
        await db.got.delete_one({"player": user_id})
        await db.shop.delete_one({"player": user_id})
        await query.message.edit_reply_markup(reply_markup=None)
        return await query.message.edit_caption(f"`ʏᴏᴜ'ʀᴇ ᴀ ɴᴇᴡʙɪᴇ ɴᴏᴡᴏɴᴡᴀʀᴅs.`")

@Hancock.on_callback_query(filters.regex("set"))
async def setprofile(_, query):
     user_id = int(query.data.split(":")[1])
     url = query.data.split(":")[2]
     xp = await get_player_xp(query.from_user.id)
     if not query.from_user.id == user_id:
         return await query.answer("ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴘʟᴀʏᴇʀ ᴡʜᴏ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛᴏ sᴇᴛ ᴘʀᴏғɪʟᴇ", show_alert=True)         
     if xp < 1000:
         return await query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴛᴏᴋᴇɴ ᴛᴏ sᴇᴛ ᴘʀᴏғɪʟᴇ.", show_alert=True)
     else:
        gone = xp - 1000
        lmao = "https://graph.org" + url
        await update_player_profile(query.from_user.id, lmao)
        await update_player_xp(query.from_user.id, gone)
        await query.message.edit_reply_markup(reply_markup=None)
        return await query.message.edit_caption(f"`ᴛʜɪs ɪᴍᴀɢᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ᴀs ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ`\n\n**ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ:** `{gone}` 🎴")

uwu = """
• **ɴᴀᴍᴇ:** `{}`
• **ɪᴅ:** `{}`
• **ᴘᴏᴋᴇᴅᴇx:** `{}`
• **sᴇʀɪᴇs:** `{}`
• **ᴀʀᴛɪsᴛ:** `{}`
• **ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴀ:** `{}`
• **ᴜᴘᴅᴀᴛᴇᴅ ᴀᴛ:** `{}`
• **ᴄᴀʀᴅ ɴᴏ**: `{}`
"""

@Hancock.on_callback_query(filters.regex("nexti"))
async def next(_, query):
     user_id = int(query.data.split(":")[1])
     pokemon_name = query.data.split(":")[2]
     q = query.data.split(":")[3]
     card = requests.get(f"https://api.pokemontcg.io/v2/cards?q=name:{pokemon_name}", headers={'X-Api-Key':'a373cfc1-3b13-46c2-bc19-fc3b7e152fb8'}).json()["data"]
     buttons = [[
         InlineKeyboardButton("Back ⏮️", callback_data=f"backi:{query.from_user.id}:{pokemon_name}:{q}"),
         InlineKeyboardButton("Next ⏭️", callback_data=f"nexti:{query.from_user.id}:{pokemon_name}:{q}") 
 ]]
     if not query.from_user.id == user_id:
         return await query.answer("ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴜsᴇʀ ᴡʜᴏ ʀᴇǫᴜᴇsᴛᴇᴅ", show_alert=True)         
     if cards:
        name = card[q+1]["name"]
        id = card[q+1]["id"]
        pokedex = card[q+1]["nationalPokedexNumbers"]
        series = card[q+1]["set"]["series"]
        artist = card[q+1]["artist"]
        rldate = card[q+1]["set"]["releaseDate"]
        updated = card[q+1]["set"]["updatedAt"]
        pic = card[q+1]["images"]["large"]
        if q+1 == len(card)-1:
            return await query.message.edit_media(
    media=InputMediaPhoto(pic, caption=uwu.format(name, id, pokedex, series, artist, rldate, updated)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Back ⏮️",callback_data=f"backi:{query.from_user.id}:{l}")]]))
        else:
           return await query.message.edit_media(
    media=InputMediaPhoto(pic, caption=uwu.format(name, id, pokedex, series, artist, rldate, updated)), reply_markup=InlineKeyboardMarkup(buttons))

@Hancock.on_callback_query(filters.regex("backi"))
async def back(_, query):
     user_id = int(query.data.split(":")[1])
     q = query.data.split(":")[2]
     h = await get_boughts(user_id)
     x = h.split(",")
     l = int(q) - int(1)
     y = x[l]
     buttons = [[
         InlineKeyboardButton("Back ⏮️", callback_data=f"backi:{query.from_user.id}:{l}"),
         InlineKeyboardButton("Next ⏭️", callback_data=f"nexti:{query.from_user.id}:{l}") 
 ]]
     if not query.from_user.id == user_id:
         return await query.answer("ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴘʟᴀʏᴇʀ", show_alert=True)         
     else:
        m = await get_shop(int(y))
        if y == x[0]:
            return await query.message.edit_media(
    media=InputMediaPhoto(m['pic'], caption=uwu.format(query.from_user.mention, l+1, m["name"], m["series"], m["date"], m["value"])), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Next ⏭️",callback_data=f"nexti:{query.from_user.id}:{l}")]]))
        else:
           return await query.message.edit_media(
    media=InputMediaPhoto(m['pic'], caption=uwu.format(query.from_user.mention, l+1, m["name"], m["series"], m["date"], m["value"])), reply_markup=InlineKeyboardMarkup(buttons))
 
@Hancock.on_message(get_command("profile"))
async def _profile(_, message):
  us_in_db = await get_player(message.from_user.id)             
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.`")
  else:
      b = await get_player_bank(message.from_user.id)
      x = await get_player_level(message.from_user.id)
      y = await get_player_xp(message.from_user.id)
      z = await get_player_profile(message.from_user.id)
      t = await get_player_total(message.from_user.id)
      p = (int(x)+1)*50
      d = await get_boughts(message.from_user.id)
      uwu = await total_items_value(message.from_user.id)
      if z == None and d:
          return await message.reply_photo(photo=random.choice(photos), caption=f"""
**🎮 {message.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍs ᴠᴀʟᴜᴇ:** `{uwu}`
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ɪᴛᴇᴍs 🛒",callback_data=f"items:{message.from_user.id}")]]))
      elif z == None and not d:
          return await message.reply_photo(photo=random.choice(photos), caption=f"""
**🎮 {message.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍs ᴠᴀʟᴜᴇ:** `{uwu}`
""")
      elif z: 
          return await message.reply_photo(z, caption=f"""
**🎮 {message.from_user.mention}'s ᴘʀᴏғɪʟᴇ:-**

**💫 ʟᴇᴠᴇʟ:** `{x}`
**⚔️ ᴘʀᴏɢʀᴇss:** `{t}`/`{p}`
**🎴 ᴛᴏᴋᴇɴ:** `{y}`
**💳 ʙᴀɴᴋ:** `{b}`
**🛍️ ɪᴛᴇᴍ ᴠᴀʟᴜᴇ:** `{uwu}`
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ɪᴛᴇᴍs 🛒",callback_data=f"items:{message.from_user.id}")]]))

hmm = """
**{}'s ɪᴛᴇᴍs!**

`1`**. ɴᴀᴍᴇ:**  `{}`  **(** `{}` **)**
**ᴜɴɪǫᴜᴇ ɪᴅ:** `{}`
**ᴠᴀʟᴜᴇ:** `{}` 🎴
"""

bitch = """
`{}`**'s ᴅᴀᴛᴀ!**

**ɴᴀᴍᴇ:**  `{}`  **(** `{}` **)**
**ᴠᴀʟᴜᴇ:** `{}` 🎴
"""

@Hancock.on_message(get_command("data"))
async def data(_, message):
  us_in_db = await get_player(message.from_user.id)   
  if not us_in_db:
    return await message.reply_text("`ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴘʟᴀʏᴇʀ`")
  else:
      if len(message.command) < 2:
          return await message.reply_text("`ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇs ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴅᴀᴛᴀ.`")          
      else:
         wager = message.text.strip().split()[1]
         x = await get_boughts(message.from_user.id)
         y = x.split(",")
         if not str(wager).isdigit():
             return await message.reply_text("`ʏᴏᴜʀ ᴠᴀʟᴜᴇ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.`")
         elif wager not in y:
             return await message.reply_text("`ʏᴏᴜ ᴄᴀɴ'ᴛ ᴀᴄᴄᴇss ᴛʜᴇ ᴅᴀᴛᴀ ᴏғ ɪᴛᴇᴍs ᴡʜɪᴄʜ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ.`")
         else:
             k = await get_shop(int(wager))
             return await message.reply_photo(k["pic"], caption=bitch.format(wager, k["name"], k["series"], k["value"]))

@Hancock.on_message(get_command("items"))
async def _items(_, message):
  us_in_db = await get_boughts(message.from_user.id)             
  if not us_in_db:
    return await message.reply_text("`ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ʙᴏᴜɢʜᴛ ᴀɴʏᴛʜɪɴɢ.`")
  else:
      x = await get_boughts(message.from_user.id)
      y = x.split(",")
      if len(y) == 1:
          kk = x.replace(",", "")
          k = await get_shop(int(kk))
          return await message.reply_photo(k["pic"], caption=hmm.format(message.from_user.mention, k["name"], k["series"], k["date"], k["value"]))
      else:
          k = await get_shop(int(y[0]))
          oo = 0
          return await message.reply_photo(k["pic"], caption=hmm.format(message.from_user.mention, k["name"], k["series"], k["date"], k["value"]), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Next ⏭️",callback_data=f"nexti:{message.from_user.id}:{oo}")]]))

@Hancock.on_message(get_command("today") & filters.user(hek))
async def _today(_, message):
  current_date = datetime.datetime.now()
  final = current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000
  name = message.text.split("-name")[1].split("-series")[0]
  series = message.text.split("-series")[1].split("-value")[0]
  value = message.text.split(None,1)[1].split()[-1]
  if not name or not series or not value or not message.reply_to_message.media:
    return await message.reply_text("`/today -pic ᴜʀʟ -name ɴᴀᴍᴇ -series sᴇʀɪᴇs -value ᴠᴀʟᴜᴇ.`")
  else:
      path = await message.reply_to_message.download()
      telegraph = upload_file(path)
      for file_id in telegraph:
          pic = "https://graph.org" + file_id
      await today_shop(final, pic, name, series, value)
      return await message.reply_text("**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴏɴᴇ.**")

@Hancock.on_message(get_command("boom") & filters.user(hek))
async def _boom(_, message):
  current_date = datetime.datetime.now()
  final = current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000
  await db.shop.delete_one({"date": final})
  return await message.reply_text("`ʙᴏᴏᴍ...`")

@Hancock.on_message(get_command("shop"))
async def _shop(_, message):
  current_date = datetime.datetime.now()
  final = current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000
  x = await get_today_shop(final)
  await add_giftp(message.from_user.id)
  b = await is_bought(message.from_user.id, f"{final}")
  money = await get_player_xp(message.from_user.id)
  us_in_db = await get_player(message.from_user.id)  
  if b == "True":
    return await message.reply_text("`ʏᴏᴜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴘᴜʀᴄʜᴀsᴇᴅ.`")
  else:
      if not us_in_db:
        return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ʙᴜʏ.`")
      if not x:
        return await message.reply_text("`ʟᴏᴏᴋ's ʟɪᴋᴇ ᴛᴏᴅᴀʏ ɴᴏᴛʜɪɴɢ ᴛᴏ sᴀʟᴇ.`")
      else:
        return await make_shop(message, x['pic'], x['name'], x['series'], x['value'], money, final)
 
@Hancock.on_callback_query(filters.regex("buy"))
async def buy(_, query):
     current_date = datetime.datetime.now()
     user_id = int(query.data.split(":")[1])
     fine = query.data.split(":")[2]
     xp = await get_player_xp(query.from_user.id)
     final = current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000
     x = await get_today_shop(final)
     if not x["date"] == final:
        return await query.answer("sᴏʀʀʏ ᴛʜɪs sᴀʟᴇ ɪs ᴇxᴘɪʀᴇᴅ", show_alert=True)         
     if xp < int(x['value']):
         return await query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴛᴏᴋᴇɴ ᴛᴏ ʙᴜʏ ᴛʜɪs", show_alert=True)
     if not query.from_user.id == user_id:
         return await query.answer("ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴘʟᴀʏᴇʀ ᴡʜᴏ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛᴏ ʙᴜʏ", show_alert=True)         
     else:
         gone = int(xp) - int(x['value'])
         await update_player_xp(query.from_user.id, gone)
         await save_bought(user_id, x["date"])
         await query.message.edit_reply_markup(reply_markup=None)
         return await query.message.edit_caption(f"`{x['name']} ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴘᴜʀᴄʜᴀsᴇᴅ`\n\n**ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ:** `{gone}` 🎴")

@Hancock.on_message(get_command("deposit") & ~filters.private)
async def _deposit(_, message):
  money = await get_player_xp(message.from_user.id)
  bb = await get_player_bank(message.from_user.id)
  us_in_db = await get_player(message.from_user.id)             
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.`")
  if not len(message.command) < 2:
    amount = message.text.split()[1]
  else:
    return await message.reply_text("`ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ᴅᴇᴘᴏsɪᴛᴇ.`")
  if not str(amount).isdigit() or int(amount) > money or int(amount) == 0:
    return await message.reply_text("`ʏᴏᴜʀ ᴅᴇᴘᴏsɪᴛ ᴀᴍᴏᴜɴᴛ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.`")
  else:
      money = int(money) - int(amount)
      await update_player_xp(message.from_user.id, money)
      await message.reply_text(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘᴏsɪᴛᴇᴅ** `{amount}` **💳 ɪɴ ᴛʜᴇ ʙᴀɴᴋ**\n\n**ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ:** `{money}` 🎴")
      amount = bb + int(amount)
      await update_player_bank(message.from_user.id, int(amount))

@Hancock.on_message(get_command("withdraw") & ~filters.private)
async def _withdraw(_, message):
  xp = await get_player_xp(message.from_user.id)
  money = await get_player_bank(message.from_user.id)
  us_in_db = await get_player(message.from_user.id)             
  if not us_in_db:
    return await message.reply_text("`ᴏɴʟʏ ᴘʟᴀʏᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ`")
  if not len(message.command) < 2:
    amount = message.text.split()[1]
  else:
    return await message.reply_text("`ɢɪᴠᴇ sᴏᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ᴡɪᴛʜᴅʀᴀᴡ.`")
  if not str(amount).isdigit() or int(amount) > money or int(amount) == 0:
    return await message.reply_text("`ʏᴏᴜʀ ᴡɪᴛʜᴅʀᴀᴡ ᴀᴍᴏᴜɴᴛ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.`")
  else:
      xp = int(amount) + xp
      money = int(money) - int(amount)
      await update_player_bank(message.from_user.id, int(money))
      await update_player_xp(message.from_user.id, xp)
      return await message.reply_text(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴡɪᴛʜᴅʀᴀᴡ** `{amount}` **🎴 ғʀᴏᴍ ᴛʜᴇ ʙᴀɴᴋ**\n\n**ʙᴀʟᴀɴᴄᴇ ɪɴ ᴛʜᴇ ʙᴀɴᴋ:** `{money}`  💳")

@Hancock.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & filters.chat(-1001328686560),
    group=1,
)
async def free(_, message):
    us_in_db = await get_player(message.from_user.id)
    if us_in_db:
        money = await get_player_xp(message.from_user.id)
        money = money + 1
        await update_player_xp(message.from_user.id, money)

@Hancock.on_message(filters.text & filters.reply, group=1)
async def chatwatchforguess(_, message):
  m = await db.memor.find_one({'mid': message.reply_to_message_id})
  if m:
    mtext = message.text.split()
    for x in mtext:
      if x not in ['/grs', '/pp', '/reverse', 'sauce']:
        if x in m['waifu']:
          await db.memor.delete_one(m)
          money = await get_player_xp(message.from_user.id)  
          money = money + 250
          await update_player_xp(message.from_user.id, money)
          await message.reply_text(f"**ᴜᴡᴜ ʏᴏᴜ ɢᴏᴛ** `250` 🎴  **ғᴏʀ ɢᴜᴇssɪɴɢ ᴄᴏʀʀᴇᴄᴛʟʏ ʏᴏᴜ'ʀᴇ ᴛʜᴇ ᴍᴀɴ/ᴡᴏᴍᴀɴ ᴏғ ᴄᴜʟᴛᴜʀᴇ.**")
