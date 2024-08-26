from database.connection import DataBaseConnection
from database.data_access import Queries
from utils import constants

db_conn = DataBaseConnection()
cursor = db_conn.conn.cursor(dictionary=True)


def fetch_properties(construction_year, city, status):
    """
       With the objetive of using SQL queries to retrieve properties with
       respective filters this method is using database collection and
       calling Queries object.

       Parameters
       ----------
       construction_year: int
           Value of construction year value
       city: str
           Value of located city of property
       status: str
           Value of status name of property
   """

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
    # Commented because same connection is calling multiple times from
    # unit test
    # finally:
    #     db_conn.close_connection()
