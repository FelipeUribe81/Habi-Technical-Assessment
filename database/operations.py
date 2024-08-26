from database.connection import DataBaseConnection
from database.data_access import Queries
from utils import constants

db_conn = DataBaseConnection()
cursor = db_conn.conn.cursor(dictionary=True)


def fetch_properties(construction_year, city, status):
    try:
        query = Queries.get_properties()
        cursor.execute(query, (
            construction_year, construction_year,
            city, city,
            status, status
        ))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching properties: {e}")
        raise e
    # finally:
    #     db_conn.close_connection()
