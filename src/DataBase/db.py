import psycopg2
import sys

from settings.const import (
    POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD,
    POSTGRES_PORT, POSTGRES_HOST
)


class DataBaseHelper():
    def __init__(self):
        self.database=POSTGRES_DB
        self.user=POSTGRES_USER
        self.password=POSTGRES_PASSWORD
        self.host=POSTGRES_HOST
        self.port=POSTGRES_PORT

    def connect_db(self):
        try:
            connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            self.cursor = connection.cursor()
            print('successful connection')
        except psycopg2.Error:
            print('Failed to setup Postgres environment.\n{0}'.format(sys.exc_info()))
