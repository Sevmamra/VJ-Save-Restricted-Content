import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26797881"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9699262c708c2e45ba18bfce925ed5ed")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sevmamra01:YSkiK1dC8vWOonX6@cluster0.ff29e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
