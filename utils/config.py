import os
from dotenv import load_dotenv

load_dotenv()


class DBConfig:
    """
       Configuration of the database collected from the environment variables

       Attributes
       ----------
       db_user: str
           Database user to connect to MySQL server
       db_password: str
           Database password to connect to MySQL server
       db_host: str
           Exposed connection address to connect to MySQL server
       db_port: int
           Port used by o MySQL server
    """

    def __init__(self):
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")


class AppConfig:
    """
       Configuration of the app collected from the environment variables

       Attributes
       ----------
       app_secret: str
           Secret value to encrypt authorization token
       app_user: str
           Username of the user that performs the request
       app_password: str
           Password of the user that performs the request
    """

    def __init__(self):
        self.app_secret = os.getenv("APP_SECRET")
        self.app_user = os.getenv("APP_USER")
        self.app_password = os.getenv("APP_PASSWORD")


db_config = DBConfig()
app_config = AppConfig()
