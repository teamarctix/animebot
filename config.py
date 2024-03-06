import os
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "HirokoRobot")
BOT_TOKEN = getenv("BOT_TOKEN", "6565729549:AAGu2-wgTtBF7WQjKUAG78cAV7RtEoZ41bc")
OWNER_ID = int(getenv("OWNER_ID", "6109551937"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6109551937 5416887843 6236996313 5218610039").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Rakesh:Meena@cluster0.0tdfk9u.mongodb.net/?retryWrites=true&w=majority")
