from pyrogram import filters , Client
from motor.motor_asyncio import AsyncIOMotorClient as async_mongo
from typing import Union
from config import *
import time
from pyrogram.types import Message


Hancock = Client(
    "Hancock",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
Hancock.start()
async_mongo_client = async_mongo(MONGO_URL)
db = async_mongo_client.Hottie



lick = ["/wager", "/wager@BoaHanCockXBot"]
@Hancock.on_message(filters.all, group=1)
async def fukkers(_, m: Message):
  bitch = await db.floodo.find_one({'chutiya': m.from_user.id})
  if not m.text in lick:
    return 
  if not bitch:
    await db.floodo.insert_one({'chutiya': m.from_user.id, 'flood': 1, 'mute': False})
  else:
    if bitch['mute']:
      if int(time.time() - bitch['time']) >= 120:
        await db.floodo.update_one(bitch, {'$set': {'mute': False, 'flood': 0}})
        await m.reply_text("`Your 2 Minutes Ignored Was Removed`")
    else:
      mf = bitch['flood'] + 1
      if mf > 15:
        await db.floodo.update_one(bitch, {'$set': {'mute': True, 'flood': mf, 'time': time.time()}})
        await m.reply_text("`You've Been Ignored For 2 Minutes`")
      else:
        await db.floodo.update_one(bitch, {'$set': {'flood': mf}})
        
async def bitchybitch(_, __, m: Message):
  bitch = await db.floodo.find_one({'chutiya': m.from_user.id})
  if bitch:
    if bitch['mute']:
      return False
  return True


floodfilter = filters.create(bitchybitch)

def get_command(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@BoaHanCockXBot"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@BoaHanCockXBot"])
  return filters.command(res, prefixes=["/", "?", "$", "!", "#", "@"]) 

def wager_command(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@BoaHanCockXBot"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@BoaHanCockXBot"])
  return filters.command(res, prefixes=["/", "?", "$", "!", "#", "@"]) & floodfilter

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return 
