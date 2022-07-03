import sqlite3

from db import get_connection

with get_connection('db_sqlite3') as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    doings_list = cursor.execute("""
            SELECT  doing.id , doing.title, doing.details, doing.date, doing.category_id, category.id
            FROM doing
            JOIN category 
            ON category_id=category.id
            WHERE doing.category_id = 6
            """).fetchone()


    print(doings_list['title'])


    # doings_list = cursor.execute("""
    #         SELECT doing.id, doing.title, doing.details, doing.date, doing.category_id
    #         FROM doing, category
    #         WHERE doing.category_id=category.id and doing.category_id = (?)
    #         """, (searching_category_id,)).fetchall()

