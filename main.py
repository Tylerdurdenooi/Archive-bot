import os
from pyrogram import Client
from os import mkdir

app_id = int(os.environ.get("API_ID", "23225789"))
app_key = os.environ.get('API_HASH', "447e207df4400d98780dcf894d975e0c")
token = os.environ.get('BOT_TOKEN', "6280249145:AAGtSXZ9UHHsszR8EsuYn6w2k37i0i0zfIA")

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
