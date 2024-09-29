import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from psycopg2.errors import UniqueViolation


class PostgresClient:
    def __init__(
        self,
        dbname="detektor",
        user="user",
        password="pass",
        host="database",
        port="5432",
    ):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
            print("PostgreSQL connection established.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None

    def executeQuery(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                self.connection.commit()
                print("Success executed query.")
            except UniqueViolation:
                return "The device_id already exists. It must be unique."
            except Exception as e:
                print(f"Error executing the query: {e}")

    def fetchQuery(self, query, data=None):
        if self.connection is None:
            print("The query cannot be executed. No connection to the database.")
            return None

        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute(query, data)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"Error executing the query: {e}")
                return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Closed connection.")
