import mysql.connector
from mysql.connector import Error
from utils.config import db_config


class DataBaseConnection:

    def __init__(self):
        self.conn = self.create_connection()

    @staticmethod
    def create_connection():
        try:
            conn = mysql.connector.connect(
                host=db_config.db_host,
                port=db_config.db_port,
                user=db_config.db_user,
                password=db_config.db_password
            )
            if conn.is_connected():
                return conn
        except Error as e:
            print(f"Error while performing connection to MySQL: {e}")
            raise e

    def close_connection(self):
        if self.conn.is_connected():
            self.conn.close()
