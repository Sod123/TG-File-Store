import os

API_ID = int(os.environ.get("API_ID", "19890227"))
API_HASH = os.environ.get("API_HASH", "ad2685e918be5a89c31e991448262e63")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5701475151:AAF6HCMZOGbxAEKF3adUVq8X3Ye_cUb9gs4")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", '-1001721596951')
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "1540312271"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001754375414')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
