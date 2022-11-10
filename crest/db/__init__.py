import psycopg2
from db.schema import Model


def init_db(config, models):
    connection = psycopg2.connect(user=config['user'],
                                  password=config['password'],
                                  host=config['host'],
                                  port=config['port'],
                                  database=config['database'])
    cursor = connection.cursor()

    for i in models:
        cursor.execute(f"CREATE TABLE {i.__name__} ( )")
