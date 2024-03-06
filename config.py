import os
from os import getenv


API_ID = int(getenv("API_ID", "25603034"))
API_HASH = getenv("API_HASH", "294a7bf4488b21609436de1cdd05c316")
BOT_USERNAME = getenv("BOT_USERNAME", "joinaccepters_bot")
BOT_TOKEN = getenv("BOT_TOKEN", "6302756306:AAEdWTi86exWgTt8Y4hUYu6IEOqvOTUQ0Y8")
OWNER_ID = int(getenv("OWNER_ID", "1881720028"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1881720028 1881720028 1881720028 1881720028").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://abcd:abcd@personalproject.mxx6dgi.mongodb.net/?retryWrites=true&w=majority")
