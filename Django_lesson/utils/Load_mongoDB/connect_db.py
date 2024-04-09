from mongoengine import connect
from decouple import config

mongo_user = config("USER")
mongodb_pass = config("PASSWORD")
db_name = config("DB_NAME")
domain = config("DOMAIN")

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)