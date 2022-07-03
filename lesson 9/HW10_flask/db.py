import json
import sqlite3


def get_connection(db_name):
    return sqlite3.connect(db_name)


def init_db(db_name):
    with get_connection(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
        DROP TABLE IF EXISTS doing;
        """)
        cursor.execute("""
        DROP TABLE IF EXISTS category;
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL)""")

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS doing(
              id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
              title VARCHAR(40) NOT NULL, 
              details VARCHAR(255), 
              date VARCHAR(40) NOT NULL, 
              category_id INTEGER NOT NULL,
              FOREIGN KEY(category_id) REFERENCES category(id))""")

        cursor.execute("""
        INSERT INTO category(name)
        VALUES ('education'), ('recreational'), ('social'), ('diy'), ('charity'), ('cooking'), ('house cleaning');
        """)

        cursor.execute("""
        INSERT INTO doing(title, details, date, category_id)
        VALUES ('Clean the window', 'detail', '2022-05-23', 7),
               ('Bake a pie with some friends', 'detail', '2022-06-23', 6)
        ;
        """)

