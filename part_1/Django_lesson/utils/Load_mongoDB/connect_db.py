from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read("E:\Git_Files\__Python_GOIT__\__Web_2_0__\Web_HW_9\Load_mongoDB\config.ini")

mongo_user = config.get("DB", "USER")
mongodb_pass = config.get("DB", "PASSWORD")
db_name = config.get("DB", "DB_NAME")
domain = config.get("DB", "DOMAIN")

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)