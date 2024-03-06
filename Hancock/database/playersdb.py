from Hancock import db
import pymongo 
from typing import Dict, List, Union


async def add_robs(date: int, player: int):
  robo = await db.robs.find_one({"date": date, "player": player})
  if robo:
    return 
  else:
    await db.robs.insert_one({"date": date, "player": player, "robs": 0})

async def get_robs(date: int, player: int):
    robs = await db.robs.find_one({"date": date, "player": player})
    if not robs:
        return None
    return robs["robs"]

async def add_got(player: int, got: str):
  players = await get_got_id()
  if player in players:
    return
  else:
    await db.got.insert_one({"player": player, "got": got})

async def get_got_id():
  player_list = []
  async for player in db.got.find({"player": {"$gt": 0}}):
    player_list.append(player["player"])
  return player_list

async def add_player(player: int, xp: int, total: int, level: int, bank: int):
  players = await get_players_id()
  if player in players:
    return
  else:
    await db.players.insert_one({"player": player, "xp": xp, "total": total, "level": level, "bank": bank ,"profile": None})

async def add_giftp(player: int):
  gifto = await get_gifto_id()
  if gifto in gifto:
    return
  else:
    await db.shop.insert_one({"player": player, "date": None})

async def get_boughts(player: int):
    bought = await db.shop.find_one({"player": player})
    if not bought:
        return None
    return bought["date"]

async def is_bought(player: int, date: str):
    bought = str(await get_boughts(player))
    b = bought.split(",")
    if date in b:
        return "True"
    return "False"

async def get_gifto_id():
  player_list = []
  async for player in db.shop.find({"player": {"$gt": 0}}):
    player_list.append(player["player"])
  return player_list

async def save_bought(player: int, date: int):
    bitch = await get_boughts(player)
    if bitch:
        mf = str(bitch) + "," + str(date)
    if not bitch or bitch == None:
        mf = str(date)
    await db.shop.update_one(
        {"player": player},
        {"$set": {"date": mf}},
    )

async def today_shop(date: int, pic: str, name: str, series: str, value: int):
    await db.shop.insert_one({"date": date, "pic": pic, "name": name, "series": series, "value": value})

async def get_shop(date: int):
  player = await db.shop.find_one({'date': date})
  if player:
    return player
  else:
    return None

async def get_today_shop(date: int):
  datte = await db.shop.find_one({"date": date})
  if datte:
    return datte
  else:
    return None

async def del_player(player: int):
  players = await get_players_id()
  if not player in players:
    return
  else:
    await db.players.delete_one({"player": player})

async def get_players_id():
  player_list = []
  async for player in db.players.find({"player": {"$gt": 0}}):
    player_list.append(player["player"])
  return player_list

async def get_player_xp(player: int):
  player = await db.players.find_one({'player': player})
  if player:
    return player['xp']
  else:
    return None

async def get_player_total(player: int):
  player = await db.players.find_one({'player': player})
  if player:
    return player['total']
  else:
    return None

async def get_player_bank(player: int):
  player = await db.players.find_one({'player': player})
  if player:
    return player['bank']
  else:
    return None

async def get_player_profile(player: int):
  player = await db.players.find_one({'player': player})
  if player:
    return player['profile']
  else:
    return None

async def get_player_level(player: int):
  player = await db.players.find_one({'player': player})
  if player:
    return player['level']
  else:
    return None

async def get_player(player: int):
  players = await get_players_id()
  if player in players:
    return True
  else:
    return False

async def get_top_players():
  player_list = []
  x = db.players.find().sort("xp", pymongo.DESCENDING)
  y = x.to_list(10)
  player_list.append(y)
  return player_list

async def add_player_level(player: int, level: int):
  players = await get_players_id()
  if player in players:
    return
  else:
    await db.players.insert_one({"player": player, "level": level})

async def update_player_xp(player: int, xp: int):
       db.players.update_one({"player": player}, {"$set":{"xp": xp}})

async def update_player_robs(date: int, player: int, robs: int):
       db.robs.update_one({"date": date, "player": player}, {"$set":{"robs": robs}})

async def update_player_total(player: int, total: int):
       db.players.update_one({"player": player}, {"$set":{"total": total}})

async def update_player_bank(player: int, bank: int):
       db.players.update_one({"player": player}, {"$set":{"bank": bank}})

async def update_player_profile(player: int, url: str):
        db.players.update_one({"player": player}, {"$set":{"profile": url}})

async def update_player_level(player: int, level: int):
       db.players.update_one({"player": player}, {"$set":{"level": level}})
