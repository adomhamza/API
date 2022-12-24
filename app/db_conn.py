import psycopg2
from psycopg2.extras import RealDictCursor
import time


while True:
    try:
        conn = psycopg2.connect(
            "host=localhost dbname=api user=postgres password=$leek",
            cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print('Database connection successful')
        break

    except Exception as err:
        print(err)
        time.sleep(5)
