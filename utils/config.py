import os
from dotenv import load_dotenv

load_dotenv()


class DBConfig:

    def __init__(self):
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")


class AppConfig:

    def __init__(self):
        self.app_secret = os.getenv("APP_SECRET")
        self.app_user = os.getenv("APP_USER")
        self.app_password = os.getenv("APP_PASSWORD")


db_config = DBConfig()
app_config = AppConfig()
